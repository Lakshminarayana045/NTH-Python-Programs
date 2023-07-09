import turtle
import colorsys

turtle.speed(0)
turtle.bgcolor("black")
turtle.pensize(2)
h=0.2
for i in range(400):
    c=colorsys.hsv_to_rbg(h,1,1)
    color(c)
    h+=0.005
    circle(i-100,80)
    done()