from random import*
import turtle

h = turtle.Turtle()
h.fillcolor("skyblue")
h.begin_fill()
h.forward(100)
h.right(90)
h.forward(100)
h.right(90)
h.forward(100)
h.right(90)
h.forward(100)
h.right(90)
h.end_fill()

h.fillcolor("royalblue")
h.begin_fill()
h.left(60)
h.forward(100)
h.right(120)
h.forward(100)
h.end_fill()

l = turtle.Turtle()
l.penup()
l.goto(-500,-100)
l.pendown()
l.write("0")
l.forward(250)
l.write("50")
l.forward(250)
l.write("100")

t = turtle.Turtle(shape = "turtle")
t.penup()
t.goto(-500,-100)
t.color("red")

g = turtle.Turtle()
g.penup()
g.goto(-350,0)
g.write("씨큐브 코딩의 타자게임!",True,font = ("arial",20,"bold"))

fruit = ["apple","banana","strawverry","watetmelon","mandarin","peach","grapes","orange","pear","kiwi"]
flower = ["rose","lily","sunflower","iris","clover","daisy","lilac","mint","ivy"]
animal = ["bear","ravvit","cat","dog","monkey","fox","wolf","lion","tiger","mouse","giraffe"]

ch = randint(0,2)
score = 0

n = randint(5,10)

if(ch == 0):
        s = choice(fruit)
        for i in range(n):
            s = choice(fruit)    
            word = turtle.textinput("fruit", '%s(%d/%d)' % (s, i+1,n))
            if(s == word):
                score += 1
elif(ch == 1):
        s = choice(flower)
        for i in range(n):
            s = choice(flower)    
            word = turtle.textinput("flower", '%s(%d/%d)' % (s, i+1,n))
            if(s == word):
                score += 1

       
else:
        s = choice(animal)
        for i in range(n):
            s = choice(animal)    
            word = turtle.textinput("animal", '%s(%d/%d)' % (s,i+1,n))
            if(s == word):
                score += 1
   
rate = score / n * 100

g.penup()
g.goto(0, - 50)
g.pendown()
g.write("%d/%d번 성공!" %(score,n),True,font = ("Arial", 15,"bold"))
g.penup()
g.goto(0,-100)
g.pendown()
g.write("정확도 : %.1f%%" % rate, True,font = ("Arial",15,"bold"))

distance = t.distance(l)/100*rate
t.speed(1)
t.forward(distance)
if(rate == 100):
    t.write("집에 데려다줘서 고마워!! ♬", False, "center", font = ("Arial",15,"bold"))
    t.left(60)
    t.right(60)
    t.left(60)
    t.right(60)
elif(rate >= 80):
     t.write("집이 코앞인데!! 한번만 더 시도해줘!!",False,"center",font = ("Arial",15,"normal"))
elif(rate >= 50):
     t.write("집에 가고싶어!! ㅠ0ㅠ",False,"center",font = ("Arial",15,"normal"))
else:
    t.color("black")
    t.right(360)
    t.write("거북이가 쓰러졌어요 ㅠ_ㅠ",False,"center",font = ("Arial",15,"normal"))

    turtle.done
    
