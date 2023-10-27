##import turtle
##
##t = turtle.Turtle()
##t.shape('turtle')
##t.penup()
##t.setx(200)
##t.write('동', font=('Arial',30))
##t.setx(-200)
##t.write('서', font=('Arial',30))
##t.setx(0)
##t.sety(-200)
##t.write('남', font=('Arial',30))
##t.sety(200)
##t.write('북', font=('Arial',30))
##t.goto(0,0)
##t.pendown()
##t.pencolor('blue')
##a = turtle.textinput('','방향을 입력해 주세요.')
##t.speed(1)
##if a == '동':
##    t.setx(200)
##elif a == '서':
##    t.setx(-200)
##elif a == '남':
##    t.sety(-200)
##elif a == '북':
##    t.sety(200)
##else:
##    t.right(360)
    
import random 

print('== 첫 번째 주사위 ==')
a1 = random.randint(1,6)
b1 = random.randint(1,6)
print('A(%s) : B(%s)' % (a1,b1))
print('== 두 번째 주사위 ==')
a2 = random.randint(1,6)
b2 = random.randint(1,6)
print('A(%s) : B(%s)' % (a2,b2))
print('== 경기 결과 == ')
a = a1 + a2
b = b1 + b2
print('A(%s) : B(%s)' % (a,b))

if(a < 10 and b < 10):
    print('모두 패배')
elif(a >= 10):
    if(b < 10):
        print('A님 승리')
    elif(a > b):
        print('A님 승리')
    elif(a == b):
        print('동점')   
    else:
        print('B님 승리')
elif(b >= 10):
    if(a <= 10):
        print('B님 승리')


   












    
