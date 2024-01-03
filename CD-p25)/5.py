f = open("example.txt","r")
while True:
    print(f.tell(),end = ' ')
    line = f.readline()
    print(line.strip())
    if not line : break
f.seek(26)
print("after setting a pointer : %d(%s)" % (f.tell(),f.read()[0]))
f.close()
