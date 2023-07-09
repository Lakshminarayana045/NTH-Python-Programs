import turtle
t = turtle . Turtle()
t . speed(100)
turtle . bgcolor("white")
for i in range(200):
    t . color("blue")
    t . circle(i)
    t . left(5)
turtle . done()