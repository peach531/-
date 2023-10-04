from random import *
a = int(input("가격:"))
s = randint(1,99) 
b = a - a * (s/100)// 10 * 10 
bg = b / 10
print("축하합니다 %s%%할인쿠폰에 당첨되셨습니다!"% (s))
print("할인된 가격: %s - %s = %s + %s(부가세) = 총 %s원" % (a,(a * (s/100)// 10 * 10),b,bg,b + bg // 10 * 10))


