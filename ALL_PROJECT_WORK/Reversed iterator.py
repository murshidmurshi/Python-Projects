a=['hey','bro','how','are','you?']
for i in a:
    print(i)
print(dir(a))   #a called iter
itr=iter(a)
itr=reversed(a)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))