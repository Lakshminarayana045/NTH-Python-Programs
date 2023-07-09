import turtle
t = turtle.Turtle()
list = ["green",
        "orange",
        "purple",
        "blue",
        "cyan"]
for i in range(200):
    t.color(list[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
turtle.mainloop()
