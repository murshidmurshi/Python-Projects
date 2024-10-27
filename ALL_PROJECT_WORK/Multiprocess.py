import time
import multiprocessing

def cal_square(number):
    for i in number:
        time.sleep(0.2)
        print('Square:'+str(i*i))


def cal_cube(number):
    for i in number:
        time.sleep(0.2)
        print('Cube:' + str(i * i*i))

if __name__ == '__main__':
    arr=[2,5,7,8]
    p1=multiprocessing.Process(target=cal_square,args=(arr,))
    p2=multiprocessing.Process(target=cal_cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print('Done')