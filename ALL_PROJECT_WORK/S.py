book={}
book['tom']={
    'name':'tom',
    'address':'kaikamba',
    'phone':9001111177
}
book['jos']={
    'name':'jos',
    'address':'bcroad',
    'phone':880051744
}

import json
p=json.dumps(book)
with open('D:\json_practise','w')as f:
    f.write(p)