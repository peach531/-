from random import *
a = [0,1,2,3,4,5]
b = choice(a)
if(b == 0):
    print('Loss!')
else:
    print('No. %s spot!' % (b))
