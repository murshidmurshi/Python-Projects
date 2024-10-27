import numpy as np
a=np.array([5,4,5])
print(a[0])
n=np.array([[2,4],[3,2],[2,3]])

print(n.ndim)     # 2 Dimension
print(n.itemsize)   #it take 4bytes
print(n.dtype)

r=np.array([[2,4],[3,2],[2,3]],dtype=np.float64)
print(r.ndim)
print(r)   #it in float type you can seen in output
print(r.dtype)
print(r.itemsize)  #it take 8 bytes
print(r.size)  #total number in r
print(r.shape) #it has 3 rows and 2 coloumn

r=np.array([[2,4],[3,2],[2,3]],dtype=complex)
print(r)





###########
#333
Zero=np.zeros((3,4))      #3 rows with 4 coloumn
print(Zero)

ones=np.ones((3,2))      #3 rows with 2 column
print(ones)



###
print(np.arange(0,5))         #range write in numpy
print(np.arange(1,5,2))     #step of 2

print(np.linspace(1,5,20))     #Linear space

n=np.array([[2,4],[3,2],[2,3]])
print(n.shape)
print(n.reshape(2,3))

print(n.ravel())   #it will make it one dimension
print('*******************************************************************************************')
print(n)      #this all not affectef by orginal array



print(n.min())       #minimum in that
print(n.max())       #maxmum in that

print(n.sum())    #total all number

# 2 axis in that
print(n.sum(axis=0))  #colomn
print(n.sum(axis=1))   #rows

print(np.sqrt(n))

a=np.array([[2,4],[3,2]])
b=np.array([[9,8],[8,7]])

print(a+b)
print(a.dot(b))
















