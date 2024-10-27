import sys
import clipboard
import json


def save_item(filepath,data):
    with open(filepath,'w')as f:
        json.dump(data,f)
save_item('test.json',{"key":"value"})



def load_item(filepath):
    with open(filepath,'r')as f:

        data=json.load(f)
        return data
load_item('test.json')
if len(sys.argv)==2:
    command=sys.argv[1]

    if command=='save':
        print('save')
    elif command=='load':
        print('load')
    elif command=='list':
        print('list')
    else:
        print('unknown commmand')
else:
    print('!!!!!!!!')