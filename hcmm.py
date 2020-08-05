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
import time
import json
import tables as tb
from LT_code import *



with open('computation_configuration.json') as f:
    parameters = json.load(f)

A_dim = parameters['A_dimension']
A_hat_dim = parameters['A_hat_dimension']
worker_load = parameters['worker_node_load_index']
interval = parameters['interval']
delta = parameters['delta']
c = parameters['c']
num_iteration = parameters['num_iteration']

comm = MPI.COMM_WORLD
world_size = comm.Get_size()
num_workers = world_size -1
node_id = comm.Get_rank()
MASTER = 0

if node_id == MASTER:
    #A_file = tb.open_file('A_matrix.h5', mode='r', title="A_matrix")
    #A = A_file.root.A
    #A = A[:,:]
    #A_file.close()
    lt_code = LT_Code(delta, c, A_dim[0] ,A_hat_dim[0])
    x = np.random.randint(3, size=(A_dim[1],1))
    decoding_time = []
    total_run_time = []
    #ground_truth = np.matmul(A,x)

    #print('lt code list indexes', lt_code.list_indexes)
    #print('lt code list degree', lt_code.list_degrees)
    #print('A', A)
    #print('x', x)
    #print(ground_truth)

if node_id != MASTER:
    A_worker_file = tb.open_file('A_worker%d.h5' %node_id, mode='r', title="A_worker%d" %node_id)
    A_worker = A_worker_file.root.A_worker
    A_worker = A_worker[:,:].astype('float32')
    #print(A_worker)
    #A_worker = A_worker[:,:]
    A_worker_file.close()
    #print(A_worker)

for k in range(num_iteration):
    comm.Barrier()
    if node_id == MASTER:


        start=time.time()
        #Send x to each worker
        #print('Start sending X')
        for j in range(num_workers):
            comm.send(x, dest = j+1, tag = k)
        #print('X sent')

        #print('Waiting results')

        aggregated_results=[]
        aggregated_rows=0
        #aggregated_rows =[]
        #print('a')
        while True:
            if(aggregated_rows>=A_hat_dim[0]):
                break;
            req = comm.irecv(source=MPI.ANY_SOURCE, tag=k)
            #print('b')
            data = req.wait()
            aggregated_results.append(data)
            aggregated_rows+=data[0][1]-data[0][0]


        #print('Getting enough results')
        #Decoding step
        #print('Start Decoding')
        start_decoding_time = time.time()
        decoded_result = lt_code.lt_decode(aggregated_results)

        #print(decoded_result)
        #print('Decoding Done')
        end_decoding_time = time.time()
        #print('Iteration %d decoding time is' %k, end_decoding_time - start_decoding_time)
        #print('Iteration %d total time is' %k, end_decoding_time - start)
        print('Iteration', k)

        decoding_time.append(end_decoding_time - start_decoding_time)
        total_run_time.append(end_decoding_time - start)

    if node_id != MASTER:
        #Recv x from master
        index = worker_load[node_id-1]
        recv_x = comm.recv(source=0, tag=k)
        #print(A_worker.dtype)
        c_time1 = time.time()
        matrixRes = np.matmul(A_worker,recv_x)
        c_time2 = time.time()
        print(node_id, c_time2-c_time1)
        data = [index, matrixRes]
        #print("Send", data)
        comm.isend(data, dest=0, tag=k)

# if node_id != MASTER:
#     A_worker_file.close()

if node_id == MASTER:
    print('average decoding time is', sum(decoding_time)/len(decoding_time))
    print('average computation time is', (sum(total_run_time)-sum(decoding_time))/len(decoding_time))
    print('average total time is', sum(total_run_time)/len(total_run_time))
