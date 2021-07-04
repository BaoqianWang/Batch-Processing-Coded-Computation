"""
@Author: Baoqian Wang
@Description: Coded Parallel MPI Matrix Multiplication

"""
from mpi4py import MPI
import sys
import numpy as np
from numpy.linalg import inv
import copy
from numpy.linalg import matrix_rank
from numpy.linalg import inv
import argparse
import time
import json
import random

random.seed(30)
np.random.seed(30)

def parse_args():
    parser = argparse.ArgumentParser("Coded Matrix Multiplication Parser")
    # Environment
    parser.add_argument("--scenario", type=str, default="batch_theory", help="computation schemes including uncoded, hcmm, load-balanced, bpcc")
    #parser.add_argument("--overhead", type=str, default="batch_2", help="if the overhead is considered, bpcc_1 not considered, bpcc_2 considered")
    return parser.parse_args()

arglist = parse_args()

with open('computation_configuration.json') as f:
    parameters = json.load(f)

A_dim = parameters['A_dimension']
worker_load = parameters[arglist.scenario]
coded_length = sum([each_load[1] - each_load[0] for each_load in worker_load])

num_iteration = parameters['num_iteration']

if(arglist.scenario == 'batch_theory'):
    worker_batch_number = parameters['bpcc_1']
else:
    worker_batch_number = parameters['bpcc_2']


# interval = parameters['interval']
# delta = parameters['delta']
# c = parameters['c']
# LEARNERS = [2,3,4,5,6]
# num_straggler = 2


comm = MPI.COMM_WORLD
world_size = comm.Get_size()
num_workers = world_size -1
node_id = comm.Get_rank()
MASTER = 0

if node_id == MASTER:
    x = np.random.randint(3, size=(A_dim[1],1),dtype='int32')
    total_run_time = []


if node_id != MASTER:
    A_worker = np.random.randint(3, size=(worker_load[node_id-1][1] - worker_load[node_id-1][0], A_dim[1]), dtype='int32')


for k in range(num_iteration):
    comm.Barrier()
    time.sleep(0.2)
    if node_id == MASTER:
        start_time=time.time()
        print(0)
        for j in range(num_workers):
            comm.send(x, dest = j+1, tag = k)
        print(1)
        aggregated_results=[]
        aggregated_rows=0

        while True:
            if(len(aggregated_results)>=coded_length):
                break
            req = comm.irecv(source=MPI.ANY_SOURCE, tag=k)
            data = req.wait()
            print(9)
            aggregated_results+=data
            temp_end_time = time.time()
            print(len(aggregated_results))
            print(temp_end_time-start_time)
        end_time = time.time()
        total_run_time.append(end_time-start_time)
        print(9)

    if node_id != MASTER:
        #Recv x from master
        start_index = worker_load[node_id-1][0]
        end_index = worker_load[node_id-1][1]
        load = end_index - start_index

        num_batch=worker_batch_number[node_id-1]

        batch_size=int(np.ceil(load/worker_batch_number[node_id-1]))

        recv_x = comm.recv(source=0, tag=k)
        print(3)

        for i in range(num_batch-1):
            c_time1 = time.time()
            matrixRes = np.matmul(A_worker[i*batch_size:(i+1)*batch_size,:], recv_x)
            print(4)
            data = []
            for j, row in enumerate(matrixRes):
                single_result=[row, j+i*batch_size]
                data.append(single_result)
            c_time2 = time.time()
            req = comm.isend(data, dest=0, tag=k)

        print(5)
        # Final batch computation result
        c_time1 = time.time()
        matrixResFinal=np.matmul(A_worker[(num_batch-1)*batch_size:,:],recv_x)
        c_time2 = time.time()
        final_data = []


        for j, row in enumerate(matrixResFinal):
            single_result = [row, j+(num_batch-1)*batch_size]
            final_data.append(single_result)

        comm.isend(final_data, dest=0, tag=k)
        print(6)
if node_id == MASTER:
    print('Mean time is', np.mean(total_run_time))
