from pathlib import Path

p=Path()
for i in p.glob('*.py'):    #print all files
    print(i)

print('\n')
path=Path('ecommerce')
print(path.exists())  #see if that path is there!