try:
    age=int(input('Age:'))

    income=1000
    amount=income/age
    print(amount)


except Exception as e:
    print('Error occured!',type(e).__name__)


except ZeroDivisionError:
    print('Age not be 0 ')

print('Welcome to all')