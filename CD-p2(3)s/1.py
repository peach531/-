def times_table(a,b):
    if a > b:
        a,b=b,a    

    for j in range(a,b+1):
        print("== %d Times ==" % j)
        
        for i in range(9):
            print("%d * %d = %d" % (j,i+1,j*(i+1)))

a = int(input('a = '))
b = int(input('b = '))
times_table(a,b)
        
