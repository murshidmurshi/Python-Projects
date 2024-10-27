import winsound,time,os

def sound():
    for i in range(2):
        for j in range(5):
            winsound.MessageBeep(1)
    time.sleep(2)
def alarm(n):
    print('Wait a',n,'second')
    time.sleep(n)
    sound()

def input_destination(user_input):
    if user_input == '1':
        user_input = int(input('Enter the desired Hour: '))
        wait_time = (user_input * 60) * 60
        alarm(wait_time)
    elif user_input == '2':
        user_input = int(input('Enter the desired mintes: '))
        wait_time = (user_input * 60)
        alarm(wait_time)
    elif user_input == '3':
        user_input = int(input('Enter the desired Second: '))
        wait_time = user_input
        alarm(wait_time)
    elif user_input=='4':

        hours = int(input('Hours: '))
        minutes = int(input('Minutes: '))
        second = int(input('Second: '))

        wait_time=user_input*60*60+user_input*60+user_input
        alarm(wait_time)
    else:
        os.system('cls')
        main()

        os.system('clear')
        main()

def main():
    print('What unit of input do you want to wait: \n1.Hour\n2.Minutes\n3.Second\n4.Combination...')
    main_input=input(':')
    input_destination(main_input)
    return

main()