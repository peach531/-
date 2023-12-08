

def find_index(str):
    a = input('Find character : ')
    i = 0
    cnt=[]
    
    for i in range(len(str)):
        if str[i]==a:
            cnt.append(i)
    if str.count(a) > 0:
        return cnt
    else:
        return None
 
str = input('string')
print(find_index(str))
                   


##    while i<len(str):
##        cnt[i] == (str.find(a))
##        str[(str.find(a))] = 0
##        i += 1
##
##    return cnt
