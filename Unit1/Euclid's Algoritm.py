# Get the first number

# NumA = int(input("Enter the first number: "))
# # Get the second number
# NumB = int(input("Enter the second number: "))
# # Divide A by B
# NumC = NumA % NumB
# print(NumC)
# NumD = NumB % NumC
# print(NumD)
# NumE = NumC % NumD
# print(NumE)

# Get the remainder and times it by B

# Repeat until 0

# If the number was 0 then the previous remainder is the GCD

NumA = int(input("Enter the first number: "))
NumB = int(input("Enter the second number: "))
NumC = None

while NumB >= 0:
    NumC = NumA % NumB
    print(NumC)

    if NumC == 0:
        print(f"The GDC is {NumB}")
        break

    NumA = NumB % NumC
    print(NumA)

    NumB = NumC % NumA
    print(NumB)






