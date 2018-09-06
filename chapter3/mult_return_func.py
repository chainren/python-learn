import math

def move(x,y,step, angle=0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny

a = int(input())

b = int(input())

x,y = move(a,b,math.pi/6)
r = move(a,b,math.pi/6)

print(x,y)

print(r)
