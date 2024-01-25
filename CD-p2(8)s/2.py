As = 0
Bs = 0
for i in range(10):
    A = int(input())
    B = int(input())
    if A < B:
        Bs += 1
    elif A > B:
        As += 1
    print("\n")

if As < Bs:
    print("B")
elif As > Bs:
    print("A")
else:
    print("D")
