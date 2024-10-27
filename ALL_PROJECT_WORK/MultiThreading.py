import time
import threading

def cal_square(numbers):
    print('Calculate square number:')
    for i in numbers:
        time.sleep(0.2)
        print('Square: ',i*i)

def cal_cube(numbers):
    print('Calculate cube number:')
    for i in numbers:
        time.sleep(0.2)
        print('Cube:',i*i*i)

arr=[2,3,8,9]
t=time.time()

t1=threading.Thread(target=cal_square,args=(arr,))
t2=threading.Thread(target=cal_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print('done in ',time.time()-t)
print('Hah,I am done with all my work now!!')

