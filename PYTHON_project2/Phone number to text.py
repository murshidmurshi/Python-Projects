Phone=input('Phone: ')
digit_mapping={
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four'
}
output=''
for ch in Phone:
    output+=digit_mapping.get(ch,'!')+' '
print(output)