#for creating file
f=open('D:\\pycharm_practise\\write_file','w')
f.write('I LOVE PYTHON')
f.close()

#for overwriting file (append something)
f=open('D:\\pycharm_practise\\write_file','a')
f.write('\nI LOVE JAVA SCRIPT')
f.close()

# for reading file
d=open('D:\\pycharm_practise\\read_file','r')
d_out=open('D:\\pycharm_practise\\write_with count','w')
for line in d:
    token=line.split(' ')
    d_out.write('word_count:'+str(len(token))+line)
f.close()
d_out.close()