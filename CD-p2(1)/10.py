def rect(w,h):
    return w * h

def tri(w,h):
    return w * h / 2

def circle(r):
    return w * h / 2

print("Choose a shape :")
print("1. Rectangle", "2. Triangle", "3. Circle", sep = '\n')
n = int(input())

if n == 1:
    w = int(input("width :"))
    h = int(input("height :"))
    area = rect(w,h)
    
if n == 2:
    w = int(input("width :"))
    h = int(input("height :"))
    area = tri(w,h)
    
if n == 3:
    w = int(input("radius:"))
    area = circle(r)

print(area)
    

