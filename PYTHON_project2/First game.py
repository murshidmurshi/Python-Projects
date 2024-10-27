print('WELCOME TO MY FIRST GAME')
name=input('What is your name? ')
age=int(input('What is your age? '))

if age>=18:
    print('you are old enough to play...')
    health=10


    want_to_play=input('Do you want to play? yes or no: ').lower()
    if want_to_play=='yes':
        print('Lets play! ')
        print('your starting with 10 health')
        left_or_right=input('First choice.. left or right (left/right)').lower()
        if left_or_right=='left':

            ans=input('You follow the path reach the lake ...Do you want to swim across or go around the (across/around)? ').lower()
            if ans == 'around':
                print('you were around and reached some side of the lake')
            elif ans=='across':
                print('Nice! you managed to across the river,were you bit by fish and you lose 5 health...')
                health-=5
            ans=input('you noticed a house and a river ,which do you go to(house/river)? ').lower()
            if ans=='house':
                print('you go to the house of owner,but he did not like you and you lose 5 health...')
                health-=5
                if health<=0:
                    print('you now have 0 health and lost the game')
                else:
                    print('you are survived and you win...')
            else:
                print('you fell down and lost...')
                print('')



        elif left_or_right=='right':
            print('you fell down and lost')
        else:
            print('Choose only left or right...')
    else:
        print('noop!!')

else:
    print('you are not enough to play game')
