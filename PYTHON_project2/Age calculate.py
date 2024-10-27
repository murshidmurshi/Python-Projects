play=input('Do you want to calculate your Current age? ')
if play=='y':
    name=input('what is your name? ')
    date_of_birth=int(input('What is your birth year? '))
    current_year=int(input('Current year? '))
    age=current_year-date_of_birth
    print('Hello '+name+',your '+str(age)+' years old')
else:
    print('Please enter y or n')
