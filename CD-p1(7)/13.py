import random
a = random.randint(1,3)
print("1 : 가위 2 : 바위 3 : 보")

b = int(input())

print("COM(%s), USER(%s)" % (a,b))
if a == b:
    print("Draw")
elif a == 1 and b == 2:
    print("Com Wins")
elif a == 2 and b == 3:
    print("Com Wins")
elif a == 3 and b == 1:
    print("Com Wins")
elif a == 2 and b == 1:
    print("Wins")
elif a == 3 and b == 2:
    print("Wins")
elif a == 1 and b == 3:
    print("Wins")
