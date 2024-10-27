#it is similar to list

import numpy as np
a=np.array([1,2,4])
#print(a)

#Compared to list numpy is very fast

import numpy as np
import time

SIZE=10000000

#python list
start=time.time()
l1=range(SIZE)
l2=range(SIZE)
result=[x+y for x,y in zip(l1,l2)]
print('python list took',(time.time()-start)*1000)

#numpy array
start=time.time()
a1=np.arange(SIZE)
a2=np.arange(SIZE)

array=a1+a2
print('Numpy array took',(time.time()-start)*1000)