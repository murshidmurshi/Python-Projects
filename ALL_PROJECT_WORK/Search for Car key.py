key_location='chair'
location=['garage','living room','chair','closet']

for i in location:
    if i==key_location:
        print('key is found in',i)
        break
    else:
        print('key is not found in',i)