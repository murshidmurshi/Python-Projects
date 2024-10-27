number=[8,8,76,9,8,3,5,6]
number2=number.copy()
print(number)
number2.append(32)
print(number2)
number.sort()
print(number)
print(30 in number )

#duplicate Number
number3=[1,2,2,2,2,24,3,2,2,7,7,5,4,4,3]
uniq=[]
for num in number3:
    if num  not in uniq:
        uniq.append(num)
print(uniq)