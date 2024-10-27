def get_digit(num):
    digit=[ ]
    while num:
        digit.append(num%10)
        num//=10
        digit.reverse()

    return digit

def is_prime_number(num):
    previous_number=[]
    while True:
        digit=get_digit(num)
        squared_digit=sum(list(map(lambda x:x**2,digit)))
        if squared_digit==1:
            return True
        elif squared_digit in previous_number:
            return False
        else:
            num=squared_digit
            previous_number.append(num)


def happy_number(num):
    happy_number=[ ]
    count=0
    while count<8:
        if is_prime_number(num):
            happy_number.append(num)
            count+=1
        num+=1
    return happy_number
print(happy_number(2))



