import turtle
colors = ["pink", "yellow", "blue", "green", "white", "red"]
sketch = turtle.pen()
turtle.bgcolor("black")
for i in range(200):
    sketch.pencolors ("color"[i%6])
    sketch.width(i/100 + 1)
    sketch.forward(i)
    sketch.left(60)
turtle.done()