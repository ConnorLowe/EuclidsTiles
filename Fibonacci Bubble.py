import turtle as t
t.speed(1)
numberOfBubbles = 0
sum = 0
diameter = 0
f1 = 0
f2 = 1
def myCircle(sz):
    t.circle(sz)

t.penup()
t.goto(-350, 0)
t.pendown()

while numberOfBubbles < 14:
    sum = f1 + f2
    f2 = f1

    f1 = sum
    diameter = sum
    # numberOfBubbles = numberOfBubbles + 1
    numberOfBubbles += 1
    myCircle(diameter)




