import numpy as np
import tables as tb


ndim = 6000000
h5file = tb.open_file('test.h5', mode='w', title="Test Array")
root = h5file.root
x = h5file.create_carray(root,'x',tb.Float64Atom(),shape=(ndim,ndim))
x[:100,:100] = np.random.random(size=(100,100)) # Now put in some data
print(x[:100,:100])
h5file.close()


h5file = tb.open_file('test.h5', mode='r', title="Test Array")
data = h5file.root.x
#x = h5file.create_carray(root,'x',tb.Float64Atom(),shape=(ndim,ndim))
print(data[:100,:100])
h5file.close()



# table = h5file.root.detector.readout
# print(table[:100,:100])
