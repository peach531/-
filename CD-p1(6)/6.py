import turtle

t = turtle.Turtle()

s = turtle.textinput('즐거운 씨큐브 코딩', '이름을 알려주세요')
t.write("%s님 반갑습니다^^" % s)

turtle.done()
