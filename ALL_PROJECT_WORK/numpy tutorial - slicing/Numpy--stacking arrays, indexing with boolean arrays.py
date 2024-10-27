import numpy as np

n=[1,2,3]
print(n[0:2])
a=np.array([2,3,4])
print(a[0:2])         #Slicing

r=np.array([[2,3,4],[5,6,7],[8,9,10]])
print(r)
print(r[:,1:3])



#itrate
t=np.array([[2,3,4],[5,6,7],[8,9,10]])
for row in t:
    print(row)

for cell in t.flat:     #flat for itrator
    print(cell)


#arrange and reshape
import numpy as np

a=np.arange(6).reshape(3,2)
print(a)
print('********************************************')
b=np.arange(6,12).reshape(3,2)
print(b)
print(np.vstack((a,b))) #######################################################################################
print(np.hstack((a,b))) #******************************************************************************************


#hsplit
s=np.arange(30).reshape(2,15)
print(s)
print(s[0])
print(s[1])
result=np.hsplit(s,3)
print(result[0])
print(result[1])


####
a=np.arange(12).reshape(3,4)
print(a)
b=a>4
print(b)         #Boolean
print(a[b])       #this will print if anything True in b

#you can also change the True =-11 whatever you want
a[b]=-11
print(a)











