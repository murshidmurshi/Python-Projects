from multiprocessing import pool
from multiprocessing.dummy import Pool
import time
import multiprocessing
from unittest import result

def square(number):
    for i in number:
        time.sleep(0.2)
        print('Square:'+str(i*i))

def cube(number):
    for i in number:
        time.sleep(0.2)
        print('Cube:'+str(i*i*i))

if __name__=='__main__':
    arr=[2,6,24,8]
    p1=multiprocessing.Process(target=square,args=(arr,))
    p2=multiprocessing.Process(target=cube,args=(arr,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Done!!!!!')
    



def f(n):
    for i in range(10000):
        return i*i

if __name__=='__main__':
    t1=time.time()
    p=Pool()
    result=p.map(f,range(10000))
    p.close()
    p.join()
    print('Pool took:',time.time()-t1)

    t2=time.time()
    sum=[]
    for i in range(100000):
        sum.append(f(i))
        
    print('Serial took:',time.time()-t2)


import calendar
print(calendar.month(2020,1))









