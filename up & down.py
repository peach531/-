import random

r = random.randint(1,100)
while(True):
    a = int(input())
    if(a > r):
        print('down')
    elif(a < r):
        print('up')
    else:
        print('correct!')
