def get_max(n):
    s = 0
    for i in range(n):
        a = int(input())
        if a > s:
            s = a
    return s

n = int(input("Enter integer n : "))

print("sum : ", get_max(n))
