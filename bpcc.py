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


random.seed(30)
np.random.seed(30)


with open('computation_configuration.json') as f:
    parameters = json.load(f)

A_dim = parameters['A_dimension']
A_hat_dim = parameters['A_hat_dimension']
num_iteration = parameters['num_iteration']
worker_load = parameters['worker_node_load_index']
worker_batch_number = parameters['worker_batch_p_value']
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
    A_file = tb.open_file('A_matrix.h5', mode='r', title="A_matrix")
    A = A_file.root.A
    A = A[:,:]
    A_file.close()
    x = np.random.randint(3, size=(A_dim[1],1))
    ground_truth = np.matmul(A,x)
    lt_code = LT_Code(delta, c, A_dim[0] ,A_hat_dim[0])


if node_id != MASTER:
    A_worker_file = tb.open_file('A_worker%d.h5' %node_id, mode='r', title="A_worker%d" %node_id)
    A_worker = A_worker_file.root.A_worker
    A_worker = A_worker[:,:]
    A_worker_file.close()

for k in range(num_iteration):
    comm.Barrier()
    if node_id == MASTER:

        start=time.time()
        #Send x to each worker
        print('Start sending X')
        for j in range(num_workers):
            comm.send(x, dest = j+1, tag = k)
        print('X sent')

        print('Waiting results')

        aggregated_results=[]
        aggregated_rows=0
        #aggregated_rows =[]
        #print('a')
        while True:
            if(aggregated_rows>=A_dim[0]):
                break;
            data=comm.recv(source=MPI.ANY_SOURCE, tag=k)
            #print(aggregated_rows)
            #print('b')
            #data = req.wait()
            #print(data[0])
            aggregated_results.append(data)
            aggregated_rows+=data[0][1]-data[0][0]


        print('Getting enough results')
        #Decoding step
        print('Start Decoding')
        start_decoding_time = time.time()
        decoded_result = lt_code.lt_decode(aggregated_results)
        print('Decoding Done')
        end_decoding_time = time.time()
        print('Iteration %d decoding time is' %k, end_decoding_time - start_decoding_time)
        print('Iteration %d total time is' %k, end_decoding_time - start)
        #print(decoded_result)
        #print(ground_truth)
        #print()
    if node_id != MASTER:
        #Recv x from master
        start_index = worker_load[node_id-1][0]
        end_index = worker_load[node_id-1][1]
        load = end_index - start_index
        num_batch=worker_batch_number[node_id-1]
        batch_size=int(np.ceil(load/worker_batch_number[node_id-1]))

        recv_x = comm.recv(source=0, tag=k)
        for i in range(num_batch-1):
            matrixRes = np.matmul(A_worker[i*batch_size:(i+1)*batch_size,:],recv_x)
            index = [start_index+i*batch_size, start_index+(i+1)*batch_size]
            data = [index, matrixRes]
            comm.send(data, dest=0, tag=k)
            #print(index, matrixRes.shape[0])

        # Final batch computation result
        matrixResFinal=np.matmul(A_worker[(num_batch-1)*batch_size:,:],recv_x)
        index = [start_index+(num_batch-1)*batch_size, end_index]
        #print(index, matrixResFinal.shape[0])
        data = [index, matrixResFinal]
        #time.sleep(3*(waitT2-waitT1))
        comm.send(data,dest=0,tag=k)
