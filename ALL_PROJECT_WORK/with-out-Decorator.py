import time

def cal_square(numbers):
    start=time.time()

    result=[]
    for i in numbers:
        result.append(i*i)
    end=time.time()
    print('cal_square took '+str(end-start*1000)+'mil sec')
    return result

def cal_cube(numbers):
    start = time.time()
    result = []
    for i in numbers:
        result.append(i * i * i)
    end=time.time()
    print('cal_cube took '+str((end-start)*1000)+'mil sec')
    return result

arr=range(1,10000)
out_square=cal_square(arr)
out_cube=cal_cube(arr)