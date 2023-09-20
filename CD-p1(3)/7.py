import turtle

t = turtle.Turtle()
t.shape('turtle')

r = 50
t.circle(r)
t.penup()
t.goto(100,0)
t.pendown()

r += 30
t.circle(r)
t.penup()
t.goto(200,0)
t.pendown()

r += 30
t.circle(r)

turtle.done
