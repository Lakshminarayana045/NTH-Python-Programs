from turtle import *
import random

setup(width=500,height=450)
colorlist = ["red","green","orange","blue","purple"]
import turtle
myturtle = turtle.Turtle()
myturtle . speed(5)
myturtle . color("blue")
myturtle . pensize(10)
myturtle . begin_fill()
for i in range(4):
    myturtle . forward(200)
    myturtle . left(90)
myturtle . end_fill()
myturtle . penup()
myturtle . forward(100)
myturtle . right(90)
myturtle . forward(40)
myturtle . color("white")
myturtle . write("ln", move=False, align="center", font=("century Gothic", 180, "bold") )
turtle . done()