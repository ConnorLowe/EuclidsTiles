import turtle as t
import random
# Task: Create a face using turtle
# Draw head
# Draw eye
# Draw nose
# Draw Rosy, red cheeks
# Draw mouth
t.speed(0)
# Move Function
def myMove(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def myCircle(sz, c): #sz = size, c = colour
    t.fillcolor(c)
    t.begin_fill()
    t.circle(sz)
    t.end_fill()

def mySemiCircle(r, sz, c): #sz = size, c = colour
    t.fillcolor(c)
    t.begin_fill()
    t.circle(sz, r)
    t.end_fill()

def myTriangle(sz): #sz = size, c = colour
    for i in range(3):
        t.forward(sz)
        t.left(120)




myCircle(100, "#f9d7a4")

myMove(-50, 100)
myCircle(20, "black")

myMove(50, 100)
myCircle(8, "white")

myMove(50, 100)
myCircle(20, "black")

myMove(39, 110)
myCircle(10, "white")

myMove(39, 110)
myCircle(10, "white")

myMove(-39, 110)
myCircle(10, "white")

myMove(-39, 110)
myCircle(10, "white")

myMove(-50, 75)
t.seth(-90)
mySemiCircle(180, 50, "black")

myMove(-50, 75)
t.seth(-90)
mySemiCircle(90, 50, "red")

myMove(-50, 75)
t.seth(-90)

t.speed(0)
t.pensize(10)



while True:
    myTriangle(random.randint(0,350))
    t.goto((random.randint(-350, 350)), (random.randint(-350, 350)))


# always use the following as the last line of code
t.ht() #hide the turtle

t.Screen().exitonclick()
