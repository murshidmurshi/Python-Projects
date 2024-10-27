import multiprocessing

def cal_square(number,result,v):
    v.value=5.67
    for idx,i in enumerate(number):
        result[idx]=i*i


if __name__ == '__main__':
    arr=[2,3,6,8]
    result=multiprocessing.Array('i',4)
    v=multiprocessing.Value('d',0.0)
    t1=multiprocessing.Process(target=cal_square,args=(arr,result,v))
    t1.start()
    t1.join()
    print(result[:])
    print(v.value)
