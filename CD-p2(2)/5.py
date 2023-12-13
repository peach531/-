def season(n):
    if n >= 3 and n <= 5:
        print('spring')
    elif n >= 6 and n <= 8:
        print('summer')
    elif n >= 9 and n <= 11:
        print('fall')
    else :
        print('winter')
n = int(input())
season(n)
    
