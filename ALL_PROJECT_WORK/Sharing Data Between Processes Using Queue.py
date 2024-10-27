import multiprocessing

def cal_square(number,q):
    for i in number:
        q.put(i*i)



if __name__ == '__main__':
    arr=[2,3,6,8]
    q=multiprocessing.Queue()
    t1=multiprocessing.Process(target=cal_square,args=(arr,q))
    t1.start()
    t1.join()
    while q.empty() is False:

        print(q.get())
