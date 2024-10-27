basket={'mango','apple','orange','apple','mango'}
print(type(basket))    # type is class --set-- and ---duplicate item removed---
print(basket)

# another one
a=set()
a.add(1)
a.add(2)
print(a)

#  if a={} its take it as a clas --dict--
# if a={'something'} somehinng in it ,it is a class --set--
# --set-- does not support index but --list-- can support
# --set-- does not allowed duplicate but --list-- can allowed




# in list you can add it--[]--
number=[1,2,1,3,4,3,2]
adding_number=set(number)
print(adding_number)
adding_number.add(29)
print(adding_number)


# set does not allowed index support
s={3,2,1,3}
# print(s[0])   #it does not support


# frozenset
number=[1,2,1,3,4,3,2]
uniq=frozenset(number)
print(uniq)

# frozenset does not allowed add new element
print(uniq.add(2))





