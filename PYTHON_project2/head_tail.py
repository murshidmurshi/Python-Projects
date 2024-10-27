import random

def Coinflip(times):
    head=0
    tail=0
    for i in range(times):
        i=random.choice([0,1])
        if i==0:
            head+=1
            print('head')
        else:

            tail+=1
            print('tail')
    print('HEAD: '+str(head))
    print('TAIL:'+str(tail))


Coinflip(100)