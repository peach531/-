f = open("example.txt","w")
for i in range(1,4):
    f.write("Line %d\n" % i)
f.close()
