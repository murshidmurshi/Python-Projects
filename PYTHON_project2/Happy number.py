def get_digit(number):
    digit = [ ]
    while number:
        digit.append(number %10)
        number //=10

    return digit

def is_happy_number(number):
    previous_number=[]
    while True:
        digit=get_digit(number)
        square_digit=sum(list(map(lambda x:x**2,digit)))
        if square_digit==1:
            return True
        elif square_digit in previous_number:
            return False
        else:
            number=square_digit
            previous_number.append(number)


def happy_number(number):
    happy_number=[]
    count=0
    while count<8:
        if is_happy_number(number):
            happy_number.append(number)
            count+=1
        number+=1
    return happy_number

print(happy_number(33) ,int(input()))


