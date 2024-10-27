x=(input('enter the number:'))
y=(input('enter the number:'))
try:
    d=x/int(y)
except ZeroDivisionError as e:
    print('Division by Zero exception')
    d=None
except Exception as e:
    print('Exception error:',type(e).__name__)
    d=None


print('Division is :',d)


