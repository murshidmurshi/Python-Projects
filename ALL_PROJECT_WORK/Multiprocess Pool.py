from multiprocessing import Pool

def f(n):
    return n*n

if __name__ == '__main__':
    p=Pool()

    array=[2,3,4,5]
    p.map(f, array)
    result=[]
    for n in array:
        result.append(f(n))
    print(result)
  #Continue in Multiprocess_Pool-2