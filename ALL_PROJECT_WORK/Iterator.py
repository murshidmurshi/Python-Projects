a=['hey','bro','how','are','you?']
for i in a:
    print(i)

print(dir(a))   #a called iter
itr=iter(a)
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))   #in that line you can find Error  in output

