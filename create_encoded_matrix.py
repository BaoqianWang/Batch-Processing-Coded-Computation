import json
import numpy as np
import tables as tb

## Read parameters
with open('computation_configuration.json') as f:
    parameters = json.load(f)

A_dim = parameters['A_dimension']
H_dim = parameters['H_dimension']
worker_load = parameters['worker_node_load']
interval = 1000
#Write A matrix file
A_matrix_file = tb.open_file('A_matrix.h5', mode='w', title="A_matrix")
A_root = A_matrix_file.root
A = A_matrix_file.create_carray(A_root,'A',tb.Float64Atom(),shape=(A_dim[0], A_dim[1]))
for i in range(0, A_dim[0], interval):
    A[i:i+interval,:] = np.random.random(size=(interval, A_dim[1])).astype('float32') # Now put in some data
    #print(x[:100,:100])


# # Read A matrix file
# A_matrix_file = tb.open_file('A_matrix.h5', mode='r', title="A_matrix")
# A_root = A_matrix_file.root
# A = A_matrix_file.root.A


# Create H matrix
H_matrix_file = tb.open_file('H_matrix.h5', mode='w', title="H_matrix")
H_root = H_matrix_file.root
H = H_matrix_file.create_carray(H_root,'H',tb.Float64Atom(),shape=(H_dim[0], H_dim[1]))
H[:,:] = np.random.random(size=(H_dim[0], H_dim[1])).astype('float32')


# Create encoded A matrix
Encode_A_matrix_file = tb.open_file('Encode_A_matrix.h5', mode='w', title="Encode_A_matrix")
Encode_A_root = Encode_A_matrix_file.root
Encode_A = Encode_A_matrix_file.create_carray(Encode_A_root,'Encode_A',tb.Float64Atom(),shape=(H_dim[0], A_dim[1]))
for i in range(0, A_dim[1], interval):
    Encode_A[:, i:i+interval] = np.matmul(H[:,:], A[:,i:i+interval])


# Create worker load matrix for each worker
worker_load_file = [tb.open_file('load_A_matrix%d.h5' %i, mode='w', title="load_A_matrix%d" %i) for i in range(len(worker_load))]
index = 0
for i in range(len(worker_load)):
    load_worker = worker_load_file[i].create_carray(worker_load_file[i].root,'Encode_A_%d' %i, tb.Float64Atom(),shape=(worker_load[i], A_dim[1]))
    load_worker = Encode_A[index:index+worker_load[i],:]
    index = index + worker_load[i]


A_matrix_file.close()
H_matrix_file.close()
Encode_A_matrix_file .close()
for i in range(len(worker_load)):
    worker_load_file[i].close()


# h5file = tb.open_file('test.h5', mode='r', title="Test Array")
# data = h5file.root.x
# #x = h5file.create_carray(root,'x',tb.Float64Atom(),shape=(ndim,ndim))
# print(data[:100,:100])
# h5file.close()
