# create a function that takes 2 numbers and MULTIPLIES them, returning the result
def multiply(num1, num2):
    print(num1 * num2)

# create a function that takes 2 numbers and DIVIDES the second from the first, returning the result
def divide(num1, num2):
    print(num1 / num2)


# create a function that takes 2 numbers and ADDS them, returning the result
def add(num1, num2):
    print(num1 + num2)

# create a function that takes 2 numbers and MINUSES the second from the first, returning the result
def subtract(num1, num2):
    print(num1 - num2)

multiply(20, 5)
divide(1000, 15)
add(65, 25)
subtract(147, 47)

variable1 = input("Choose an Operation [m/d/a/s]: ")

if variable1 == "m":
    multiply(num1, num2)
if variable2 == "d":
    divide(num1, num2)
if variable3 == "a":
    add(num1, num2)
if variable4 == "s":
    subtract(num1, num2)

