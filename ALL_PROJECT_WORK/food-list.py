Food=input('Enter the food name:')
indian=['samosa','daal','laddu']
saudi=['mandi','beef fry','biriyani']
italy=['pizza','burger','kfc']

if Food in indian:
    print('Its belong to Indian')
elif Food in saudi:
    print('Its belong to Saudi')
elif Food in italy:
    print('Its belong to Italy')
else:
    print("I don't know which contries food is "+Food)
    print('Sry for that!')