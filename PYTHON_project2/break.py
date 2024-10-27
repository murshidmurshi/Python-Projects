print('BREAK')
#__break
x=0
while x<10:
    if x==6:
        break
    print(x)
    x=x+1
print('CONTINUE')
#__continue
x='sammy'
for item in x:
    if item=='a':
        continue
    print(item)

print('PASS')
#___pass
item=[1,2,4,5,6]
for i in item:
    pass
print('End of script')
