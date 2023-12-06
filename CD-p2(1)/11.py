def calculator(x,sb,y):
    if sb == '+':
        return x + y
    elif sb == '-':
        return x - y
    elif sb == '*':
        return x * y
    elif sb == '/':
        return x // y

a = input().split()

a[0] = int(a[0])
a[2] = int(a[2])

print("%d %c %d = %d"%(a[0],a[1],a[2],calculator(a[0],a[1],a[2])))
