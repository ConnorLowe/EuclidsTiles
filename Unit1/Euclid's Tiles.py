import turtle
t = turtle.Turtle()
t.speed(2)
t.hideturtle()
L = 345
W = 150
numberOfTilesX = 345/15
numberOfTilesY = 150/15
x = -100
y = -100
s1 = 0
s2 = 0
c = "Blue"
tilesX = 0
tilesY = 0
s = 15
def MySquare1(s1, s2, c, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(c)
    t.forward(s1)
    t.seth(90)
    t.forward(s2)
    t.seth(180)
    t.forward(s1)
    t.seth(-90)
    t.forward(s2)

def MySquare2(s, c, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(c)
    t.forward(s)
    t.seth(90)
    t.forward(s)
    t.seth(180)
    t.forward(s)
    t.seth(-90)
    t.forward(s)


MySquare1(L, W, c, x, y)
while tilesX < numberOfTilesX:
    MySquare2(s, x, y, c)
    t.penup()
    t.goto(x, y)
    t.pendown()
    x += s
    tilesX += 1

while tilesY < numberOfTilesY:
    MySquare2(s, x, y, c)
    t.penup()
    t.goto(x, y)
    t.pendown()
    y += -s
    tilesY += 1




