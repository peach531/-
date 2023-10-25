import random
com = random.randint(1,2)
user = int(input('odd : 1, even : 2\n'))

if user == 1:
    print('USER(%s) ' % ('odd'))
if user == 2:
    print('USER(%s) ' % ('even'))
if com == 1:
    print('COM(%s) ' % ('odd'))
if com == 2:
    print('COM(%s) ' % ('even'))
    
if com == user :
    print('Correct')
else:
    print('Incorrect')
