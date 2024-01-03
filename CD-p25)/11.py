f = open("alphabet.txt","r")
index = int(input("index :"))
f.seek(index)
while True :
    line = f.readline()
    if not line : break
    print(line,end = '')
f.close()
