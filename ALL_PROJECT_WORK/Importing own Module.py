#inside ,from same project
import  FUNCTION as f
sq=f.square(10)
print(sq)
sm=f.sum(10,20)
print(sm)

#from other file

from j import nj as x
d=x.divition(20,5)
print(d)

#import from system
import  sys
sys.path.append('C:\code')
