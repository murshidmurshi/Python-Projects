import random
print('WElCOME TO MY FIRST GAME!!')
name=input('What is your name? ')
age=int(input('What is your age? '))
if age>10:
    print('Your old enough to play ')
else:
    print('your still child ')

play=input('DO you want to play? yes or no :')

if play.lower() == 'yes':
    print('your starting with 10 health ')
    select = input(
        'You follow the path reach the lake ...Do you want to swim across or go around the (across/around)? ')
    if select.lower() == 'across':
        print('you manged to across, But were bit by fish and you lost 5 health ..')
        s = input('you noticed a house and a river ,which do you go to(house/river)? ')
        if s.lower() == 'river':
            print('were you bit by fish again,You lost')
        elif s.lower() == 'house':
            print('you saved you life and you won  ')

    else:
        print('you fell down and lose')

elif play.lower() == 'no':
    print('Take time and come back to play ')
