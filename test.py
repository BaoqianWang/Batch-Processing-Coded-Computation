import numpy as np
import time

x = np.random.randint(3, size=(40000,1))
A = np.random.randint(3, size=(200, 40000))
B = np.random.randint(3, size=(1,40000))

start=time.time()
np.matmul(A,x)
end=time.time()
print('time is ', end-start)


start1=time.time()
for _ in range(200):
    np.matmul(B, x)
end1=time.time()
print('time 2 is', end1-start1)
