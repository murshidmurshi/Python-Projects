import sys
import clipboard
import json

SAVED_DATA="test.json"

def save_item(filepath,data):
    with open(filepath, "w")as f:
        json.dump(data,f)
save_item('ss.json',{"key":"ss"})

def read_item(filepath):
    with open(filepath,"r")as f:
        data=json.load(f)
        return data
read_item("ss.json")




if len(sys.argv)==2:
    command=sys.argv[1]
    data=read_item(SAVED_DATA)
    if command=='save':
        key=input('enter the key: ')
        data[key]=clipboard.paste()
        save_item(SAVED_DATA,data)
    elif command=='file':
        print('file')
    elif command=='load':
        print('load')
else:
    print('none')