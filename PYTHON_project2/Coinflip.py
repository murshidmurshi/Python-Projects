import random

def Coinflip(times):
    head=0
    tail=0
    for i in range(times):
        i=random.choice([0,1])
        if i==0:
            head+=1
            print('Head ')
        else:
            tail+=1
            print('Tails ')
    print('HEAD: '+str(head))
    print('TAILS: '+str(tail))
Coinflip(190)