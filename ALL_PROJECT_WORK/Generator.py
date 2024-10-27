#Generator are simply way to create iterator
#Generator attomatically raise StopIterator exception
def remote_control_list():
    yield 'HBO'
    yield 'CNN'

iter=remote_control_list()
print(next(iter))
print(next(iter))
print(next(iter))
print('*********')
# we can also print like
for i in remote_control_list():
    print(i)