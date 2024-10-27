customer={
    'name':'Murshid',
    'age':18,
    'gmail':'murshid03@gamil.com'
}
print(customer['name'])
print(customer['gmail'])
customer['Area']='Bc road' #modified 

for item in customer:
    print(item)



print('\n')
print(customer.get('birthday'))

print(customer.get('birthday','Jan 28,2004'))
