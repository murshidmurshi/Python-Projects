import sys
import clipboard
import json

clipboard.copy('aaa')
s=clipboard.paste()
print(s)