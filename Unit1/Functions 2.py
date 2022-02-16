v = input("Choose an Operation [m/d/a/s]: ")
# create a function that takes 2 numbers and MULTIPLIES them, returning the result
def multiply(num1, num2):
    if v == "m":
        print(num1 * num2)

# create a function that takes 2 numbers and DIVIDES the second from the first, returning the result
def divide(num1, num2):
    if v == "d":
        print(num1 / num2)


# create a function that takes 2 numbers and ADDS them, returning the result
def add(num1, num2):
    if v == "a":
        print(num1 + num2)

# create a function that takes 2 numbers and MINUSES the second from the first, returning the result
def subtract(num1, num2):
    if v == "s":
        print(num1 - num2)

multiply(20, 5)
divide(1000, 15)
add(65, 25)
subtract(147, 47)
