n=False
o=''
while True:
    o = input('> ').lower()
    if o=='start':
        if n:
         print('&&&&&&&')
        else:
            n=True
            print('********')

    elif o=='stop':
        if not n:
            print("??????????")
        else:
            n=False
            print('>>>>>>>>>')