exp=[100,200,300]
#total=exp[0]+exp[1]+exp[2]
#print(total)

#Another method
exp=[100,200,300]
total=0
for item in exp:
    total=total+item
print(total)


#extra thing in total exercise
exp=[100,200,300]
total=0
for i in range(len(exp)):
    print('month:',i+1,'expenses:',exp[i])
    total=total+exp[i]
print('Total expences is',total)









#print 1-10
for i in range(1,11):
    print(i)
