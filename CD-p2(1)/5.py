def get_sum(n,m):
    s = 0
    for i in range(m,n+1,1):
        s += i
    return s

m = int(input())
n = int(input())
print("%d부터 %d까지 합은 %d입니다." % (m,n,get_sum(n,m)))
