print("===== menu =====\n1.burger\n2.sandwitch\n3.Hotdog\n4.coke\n5.milk\n================")
a = int(input())
if a == 1:
    print("Burgers ar not available")
elif a == 2 or a== 3:
    print("What would you like to drink")
elif a == 4:
    print("I like coke, to")
else:
    print("Would you like hot or cold")
