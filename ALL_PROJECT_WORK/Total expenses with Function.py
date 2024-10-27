#Without function
toms_expences=[100,300,500]
jos_expences=[600,600,100]

total=0
for item in toms_expences:
    total=total+item
print('toms expences is',total)
total=0
for item in jos_expences:
    total=total+item
print('jos expences is',total)

#with Function
def calculation(exp):
    total=0
    for item in exp:
        total=total+item
    return total
toms_expences=[100,300,500]
jos_expences=[600,600,100]

toms_total=calculation(toms_expences)
jos_total=calculation(jos_expences)

print('toms expences is',toms_total)
print('jos expences is',jos_total)