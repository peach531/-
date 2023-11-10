from random import *

user = 5
wn = 0
count = 0
up = ' '
cp = ' '
rcp = ['가위','바위','보']
u = []
while(wn <= user-1):
    u.append(choice(rcp))
    wn += 1

c = []
wn = 0
while(wn <= user-1):
    c.append(choice(rcp))
    wn += 1
wn = 0

print('플레이어 카드:')
print(u)
print('\n')

while(user < 1):
    print('가위 바위 보!')
    up = choice(u)
    print('%s\n' % up)
    cp = choice(c)
    print('----승부 결과----\n')
    if()
    
    

