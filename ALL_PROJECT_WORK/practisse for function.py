def sum(a,b):
    '''
    this is the function that take two integer
    and return sum of them as output
    '''
    print('a:',a)
    print('b:',b)
    total=a+b
    print('total inside function:',total)
    return total
n=sum(5,6)
print('total ouside function:',n)