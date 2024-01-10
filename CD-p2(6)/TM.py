H = int(input("시 입력: "))
M = int(input("분 입력: "))
S = int(input("초 입력: "))
T = int(input("돌아갈 시간 초  입력: "))

S = S - T % 60
T = T / 60
if T > 59:
    H = H - T / 60
    M = M - T % 60
else:
    M = M - T

if S < 0:
    S = 59
    M -= 1
elif M < 0:
    M = 59
    H -= 1
    
print("돌아간 시간은 %d시 %d분 %d초입니다" % (H,M,S))
    

