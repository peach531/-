f = open("profile.txt","r")
f.seek(31)
while True :
    line = f.readline()
    if not line : break
    print(line, end = '')
f.close
