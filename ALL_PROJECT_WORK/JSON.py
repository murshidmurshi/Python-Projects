book={}
book['tom']={
    'name':'tom',
    'address':'kaikamba',
    'phone':899898989
}

book['jos']={
    'name':'jos',
    'address':'bcroad',
    'phone':454566545
}

import json
m=json.dumps(book)
print(m)

f=open('D:\json_practise','w')
g=f.write(m)

