import json
import numpy as np
import tables as tb
from LT_code import *
import argparse

def parse_args():
    parser = argparse.ArgumentParser("Coded Matrix Multiplication Parser")
    # Environment
    parser.add_argument("--scenario", type=str, default="uncoded", help="computation schemes including uncoded, hcmm, load-balanced, bpcc")
    return parser.parse_args()

arglist = parse_args()


## Read parameters
with open('computation_configuration.json') as f:
    parameters = json.load(f)

A_dim = parameters['A_dimension']
A_hat_dim = parameters['A_hat_dimension']
worker_load = parameters[arglist.scenario]
interval = parameters['interval']
delta = parameters['delta']
c = parameters['c']
lt_code = LT_Code(delta, c, A_dim[0] ,A_hat_dim[0])
#Create A matrix file
A_matrix_file = tb.open_file('A_matrix.h5', mode='w', title="A_matrix")
A_root = A_matrix_file.root
A = A_matrix_file.create_carray(A_root,'A',tb.Float64Atom(),shape=(A_dim[0], A_dim[1]))
for i in range(0, A_dim[0], interval):
    A[i:i+interval,:] = np.random.randint(4,size=(interval, A_dim[1])).astype('float32')
    #random(size=(interval, A_dim[1])).astype('float32') # Now put in some data
    #print(x[:100,:100])
#print(A[:,:])
# Create encoded A matrix
# Open matrix file
Encode_A_matrix_file = tb.open_file('Encode_A_matrix.h5', mode='w', title="Encode_A_matrix")
Encode_A_root = Encode_A_matrix_file.root
Encode_A = Encode_A_matrix_file.create_carray(Encode_A_root,'Encode_A',tb.Float64Atom(),shape=(A_hat_dim[0], A_hat_dim[1]))

# Start encoding

#print(lt_code.list_indexes)
for i in range(A_hat_dim[0]):
    #selection_indexes = sample_indexes(i, lt_code.random_degrees[i], A_dim[0])
    selection_indexes = lt_code.list_indexes[i]
    Encode_A[i, :] = np.sum(A[selection_indexes, :],axis=0)
    #print('selection indexes', selection_indexes)
    #print(A[selection_indexes, :])
    #print(np.sum(A[selection_indexes, :], axis=0))
#print('Encoded A', Encode_A[:,:])

# Create worker load matrix for each worker
worker_load_file = [tb.open_file('A_worker%d.h5' %(i+1), mode='w', title="A_worker%d" %(i+1)) for i in range(len(worker_load))]
index = 0
for i in range(len(worker_load)):
    load_worker = worker_load_file[i].create_carray(worker_load_file[i].root,'A_worker', tb.Float64Atom(),shape=(worker_load[i][1]-worker_load[i][0], A_dim[1]))



    load_worker[:,:] = Encode_A[worker_load[i][0]:worker_load[i][1],:]
    #print(load_worker)

A_matrix_file.close()
Encode_A_matrix_file .close()
for i in range(len(worker_load)):
    worker_load_file[i].close()



# symbol = Symbol(index=i, random_degrees[i], encoded_row)
# encoded_A_symbol.append(symbol)

# for i in range(m):
#     Encode_A[:, ] = np.matmul(H[:,:], A[:,i:i+interval])





# # Read A matrix file
# A_matrix_file = tb.open_file('A_matrix.h5', mode='r', title="A_matrix")
# A_root = A_matrix_file.root
# A = A_matrix_file.root.A


# # Create H matrix
# H_matrix_file = tb.open_file('H_matrix.h5', mode='w', title="H_matrix")
# H_root = H_matrix_file.root
# H = H_matrix_file.create_carray(H_root,'H',tb.Float64Atom(),shape=(H_dim[0], H_dim[1]))
# H[:,:] = np.random.random(size=(H_dim[0], H_dim[1])).astype('float32')
#
#
# # Create encoded A matrix
# Encode_A_matrix_file = tb.open_file('Encode_A_matrix.h5', mode='w', title="Encode_A_matrix")
# Encode_A_root = Encode_A_matrix_file.root
# Encode_A = Encode_A_matrix_file.create_carray(Encode_A_root,'Encode_A',tb.Float64Atom(),shape=(H_dim[0], A_dim[1]))
# for i in range(0, A_dim[1], interval):
#     Encode_A[:, i:i+interval] = np.matmul(H[:,:], A[:,i:i+interval])
#
#
# # Create worker load matrix for each worker
# worker_load_file = [tb.open_file('A_worker%d.h5' %(i+1), mode='w', title="A_worker%d" %(i+1)) for i in range(len(worker_load))]
# index = 0
# for i in range(len(worker_load)):
#     load_worker = worker_load_file[i].create_carray(worker_load_file[i].root,'A_worker', tb.Float64Atom(),shape=(worker_load[i], A_dim[1]))
#     load_worker = Encode_A[index:index+worker_load[i],:]
#     index = index + worker_load[i]
#
#
# A_matrix_file.close()
# H_matrix_file.close()
# Encode_A_matrix_file .close()
# for i in range(len(worker_load)):
#     worker_load_file[i].close()
