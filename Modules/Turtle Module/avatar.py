from turtle import *
speed(0)
bgcolor('white')
color('black')
hideturtle()
n = 1
p = True
while True:
    circle(n)
    if p:
        n = n-1
    else:
        n = n+1
    if n==0 or n==60:
         p=not p
         left(1)
         forward(3)
         left(2)
         forward(4)
turtledone()