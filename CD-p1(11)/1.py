m = 5
n = int(input('정수 : '))
for j in range(5):
    for h in range(m):
        print(" ",end = ' ')
    print()
    m -= 1
m = 1
for i in range(n):
    for a in range(m):
        print("*",end = ' ')
    print()
    m += 1
