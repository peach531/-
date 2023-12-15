def d(n):
    if n % 2 == 0:
        print(n)
        n -= 1
    elif n == 1:
        return 
        
    else:
        n -= 1
    d(n)

n = 10
print(d(n))
    
