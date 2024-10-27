# List
number=[1,2,3,4,6,8,9]
even=[]
for i in number:
    if i%2==0:
        even.append(i)

print(even)

#List comprehension
number=[1,2,3,4,6,8,9]
even=[i for i in number if i%2==0]
print(even)

sqrt=[i*i for i in number ]
print(sqrt)


#set --Duplicate item removed
s=set([1,2,3,4,53,2,3,2,1,5])
print(s)
r={i for i in s if i%2==0}   #Even Formula
print(r)

#Example  Zip
cities={'Mumbai','new york','paris'}
contries={'india','usa','france'}
z=zip(cities, contries)
print(z)

for i in z:
    print(i)
d={cities:contries for cities,contries in zip(cities, contries)}
print(d)
