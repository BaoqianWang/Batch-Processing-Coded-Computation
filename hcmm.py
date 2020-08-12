"""
@Author: Baoqian Wang
@Description: Coded Parallel MPI Matrix Multiplication

"""

from mpi4py import MPI
import sys
import numpy as np
from numpy.linalg import inv
import copy
import argparse
from numpy.linalg import matrix_rank
from numpy.linalg import inv
import time
import json
import tables as tb
from LT_code import *

random.seed(30)
np.random.seed(30)


def parse_args():
    parser = argparse.ArgumentParser("Coded Matrix Multiplication Parser")
    # Environment
    parser.add_argument("--scenario", type=str, default="hcmm", help="computation schemes including uncoded, hcmm, load-balanced, bpcc")
    return parser.parse_args()

arglist = parse_args()



with open('computation_configuration.json') as f:
    parameters = json.load(f)


A_dim = parameters['A_dimension']
worker_load = parameters[arglist.scenario]
coded_length = sum([each_load[1] - each_load[0] for each_load in worker_load])



interval = parameters['interval']
delta = parameters['delta']
c = parameters['c']
num_iteration = parameters['num_iteration']
LEARNERS = [2,3,4,5,6]
num_straggler = 1

comm = MPI.COMM_WORLD
world_size = comm.Get_size()
num_workers = world_size -1
node_id = comm.Get_rank()
MASTER = 0

if node_id == MASTER:
    # A_file = tb.open_file('A_matrix.h5', mode='r', title="A_matrix")
    # A = A_file.root.A
    # A = A[:,:]
    #A_file.close()
    lt_code = LT_Code(delta, c, A_dim[0] , coded_length)
    x = np.random.randint(3, size=(A_dim[1],1))
    #decoding_time = []
    total_run_time = []
    #ground_truth = np.matmul(A,x)

    #print('lt code list indexes', lt_code.list_indexes)
    #print('lt code list degree', lt_code.list_degrees)
    #print('A', A)
    #print('x', x)
    #print(ground_truth)

if node_id != MASTER:
    #A_worker_file = tb.open_file('A_worker%d.h5' %node_id, mode='r', title="A_worker%d" %node_id)
    #A_worker = A_worker_file.root.A_worker
    #A_worker = A_worker[:,:].astype('float32')
    #print(A_worker)
    A_worker = np.random.randint(3, size=(worker_load[node_id-1][1] - worker_load[node_id-1][0],A_dim[1]), dtype='int32')
    #A_worker = A_worker[:,:]
    #A_worker_file.close()
    #print(A_worker)

for k in range(num_iteration):
    comm.Barrier()
    time.sleep(0.2)
    straggler_node_id = random.sample(LEARNERS, num_straggler)
    if node_id == MASTER:
        start_time=time.time()
        #Send x to each worker
        #print('Start sending X')
        print(0)
        for j in range(num_workers):
            comm.send(x, dest = j+1, tag = k)
        #print('X sent')
        #print('Waiting results')

        aggregated_results=[]
        aggregated_rows=0
        #aggregated_rows =[]
        #print('a')
        while True:
            if(len(aggregated_results)>=coded_length):
                break
            data = comm.recv(source=MPI.ANY_SOURCE, tag=k)
            aggregated_results+=data
            temp_end_time = time.time()
            print(len(aggregated_results))
            print(temp_end_time-start_time)
        end_time = time.time()

        # print(len(aggregated_results))
        # print(end_time-start_time)
        #print(aggregated_results)

        #start_decoding_time = time.time()
        #if(arglist.scenario=='hcmm'):
            #decoded_result = lt_code.lt_decode(aggregated_results)
        #end_decoding_time = time.time()
        #decoding_time.append(end_decoding_time - start_decoding_time)
        #print(decoded_result)
        # print('Decoding Done')
        #
        # print('Iteration %d decoding time is' %k, end_decoding_time - start_decoding_time)
        # print('Iteration %d total time is' %k, end_decoding_time - start)
        # print('Iteration', k)


        #total_run_time.append(end_decoding_time - start)

    if node_id != MASTER:
        #Recv x from master
        index = worker_load[node_id-1]
        recv_x = comm.recv(source=0, tag=k)
        #print(A_worker.dtype)

        c_time1 = time.time()
        matrixRes = np.matmul(A_worker,recv_x)
        data = []
        for i, row in enumerate(matrixRes):
            single_result=[row, i+index[0]]
            data.append(single_result)
        c_time2 = time.time()


        if (node_id in straggler_node_id):
            time.sleep(3*(c_time2-c_time1))

        # Send computation data
        comm.send(data, dest=0, tag=k)

# if node_id != MASTER:
#     A_worker_file.close()

# if node_id == MASTER:
#     print('average decoding time is', sum(decoding_time)/len(decoding_time))
#     print('average computation time is', (sum(total_run_time)-sum(decoding_time))/len(decoding_time))
#     print('average total time is', sum(total_run_time)/len(total_run_time))
