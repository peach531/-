from tkinter import *
from random import *

# 라켓을 위로 이동하는 함수
def move_up(event) :
    global x, y
    y -= 25
    canvas.coords(racket, x, y)

# 라켓을 아래로 이동하는 함수
def move_down(event) :
    global x, y
    y += 25
    canvas.coords(racket, x, y)

# 공을 움직이는 함수
def move_ball() :
    global x1, y1, x2, y2, x_dist, y_dist, canvas_w, canvas_h

    # 공의 가로, 세로 길이 초기화하기
    width, height = 30, 30

    # 공이 위쪽 벽에 충돌하면 반대쪽으로 방향 바꾸기
    if y1 <= 5 :
        y1 = 5
        y_dist *= -1

    # 공이 아래쪽 벽에 충돌하면 반대쪽으로 방향 바꾸기
    if y1 >= (canvas_h - (height - 5)) :
        y1 = canvas_h - (height - 5)
        y_dist *= -1

    # 공이 왼쪽 벽에 충돌하면 방향 바꾸기
    if x1 <= 5 :
        x_dist *= -1

    # 공이 오른쪽 벽에 충돌하면 방향 바꾸기
    if x1 + width >= canvas_w - 5 :
        x_dist *= -1
        
    # 공 이동 좌표 저장하기
    x1 += x_dist
    y1 += y_dist
    x2 = x1 + width
    y2 = y1 + height
    
    # 공 위치 변경하기
    canvas.coords(ball, x1, y1, x2, y2)


# 공과 라켓의 충돌을 감지하는 함수
def detect_collision() :
    global x1, y1, x2, y2, x, y, x_dist
    
    # 라켓의 왼쪽 위 꼭짓점 좌표 초기화하기
    left, top = x, y

    # 라켓의 오른쪽 아래 꼭짓점 좌표 초기화하기
    right, bottom = x + 53, y + 121  

    # 라켓과 공의 충돌 감지하기
    if y2 > top and y1 < bottom and x2 > left and x1 < right :
        # 라켓의 오른쪽에 충돌했을 때 처리하기
        if left < x2 and (y2 > top or y1 < bottom) :
            # 공을 랜덤한 각도로 튕기기
            x1 -= randint(0, 10)
            # 공 왼쪽으로 이동
            x_dist *= -1
        # 라켓의 왼쪽에 충돌했을 때 처리하기
        if right > x1 and (bottom > y1 or top < y2) :
            # 공을 랜덤한 각도로 튕기기 
            x1 += randint(0, 10)

# 게임 진행 함수
def play_game() :
    move_ball()
    detect_collision()
    win.after(60, play_game)

# 라켓의 처음 위치 초기화하기
x, y = 235, 235

# 공의 처음 위치 초기화하기
x1, y1 = 10, 10
x2, y2 = x1 + 30, y1 + 30

# 공의 속도 초기화하기
x_dist, y_dist = 15, 15

#캔버스의 크기 초기화하기
canvas_w, canvas_h = 500, 500

win = Tk()
canvas = Canvas(win, width = canvas_w, height = canvas_h, bg = "white")
img = PhotoImage(file = "red_racket.png")
racket = canvas.create_image(x, y, image = img)
ball = canvas.create_oval(x1, y1, x2, y2, fill = "yellow")
canvas.pack()

# 게임 진행 함수 호출하기
play_game()
win.bind("<Up>", move_up)
win.bind("<Down>", move_down)
win.mainloop()
