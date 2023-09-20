a = int(input("a : "))
b = int(input("b : "))

import turtle

t = turtle.Turtle()
t.shape("turtle")

t.stamp()
t.circle(a,b)
stmp1 = t.stamp()
t.circle(a,b)
t.stamp()
t.circle(a,b)
stmp2 = t.stamp()
t.circle(a,b)

t.clearstamp(stmp1)
t.clearstamp(stmp2)
