import multiprocessing
square_result=[]
def cal_square(number):
    global square_result
    for i in number:
        print('Square:'+str(i*i))
        square_result.append(i*i)
    print('within process'+str(square_result))

if __name__ == '__main__':
    arr=[2,5,7,8]
    p1=multiprocessing.Process(target=cal_square,args=(arr,))

    p1.start()

    p1.join()
    print('result'+str(square_result))
    print('Done')