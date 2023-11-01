from random import *
a = [1,2,3,4,5,6,7,8,9,10]
ar = choices(a,[2,2,2,2,2,2,99,2,2,2],k = 3)
print(ar)
c = ar.count(7)
if(c == 3):
    print('Lucky!')
elif(c == 2):
    print('Good~')
else:
    print('So so')
