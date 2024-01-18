s = int(input())
b = int(input())
p = int(input())
B = 0
S = 0

b += p

if b > 60:
    B = b % 60
    S = s + b / 60
if S >= 24:
    S = S - 24

S = int(S)
print(S,B)
