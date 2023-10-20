#c = {'plus' : ['더하기', '장점'],'minus' : ['빼기','적자'],'multiply' : ['곱하다','다양하게'],'division' : ['나누기','분열'],'square' : ['제곱']}
#a = input("단어 : ")
#del c[a]
#print(c)

import turtle
from random import*
  

t = turtle.Turtle()

a = ['red','yellow','green','blue']
t.fillcolor(a[randint(0,3)])
t.begin_fill()
t.circle(randint(10,100))
t.forward(100)
t.end_fill()
t.fillcolor(a[randint(0,3)])
t.begin_fill()
t.circle(randint(10,100))
t.forward(100)
t.end_fill()
t.fillcolor(a[randint(0,3)])
t.begin_fill()
t.circle(randint(10,100))
t.forward(100)
t.end_fill()
t.fillcolor(a[randint(0,3)])
t.begin_fill()
t.circle(randint(10,100))
t.forward(100)
t.end_fill()





