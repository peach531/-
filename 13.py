n = int(input('n = '))

for i in range(2,n+1):
    cnt = 1
    for j in range(2,i):
        if i % j == 0:
           cnt = 0
        
    if cnt == 1:
        print(i,end = ' ')
        
        
    
    
