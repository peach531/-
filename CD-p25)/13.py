f = open("anna.txt","r")
lines = f.readline()
lines = lines.split()
for word in lines:
    if 'b' in word :
        print(word)
f.close
