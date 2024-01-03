f = open("fruit.txt","r")
word = f.readlines()

for i in word:
    i = i.strip()
    if len(i) >= 10:
        print(i)
f.close()
