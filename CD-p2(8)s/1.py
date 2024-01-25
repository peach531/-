from random import *

o = randint(0,1)
t = randint(0,1)
tr = randint(0,1)
f = randint(0,1)

a = o + t + tr + f

print(a)

if a == 1:
    print("A")
elif a == 2:
    print("B")
elif a == 3:
    print("C")
elif a == 4:
    print("D")
else:
    print("E")
