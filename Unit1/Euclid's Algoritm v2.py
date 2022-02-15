NumA = int(input("Enter the first number: "))
NumB = int(input("Enter the second number: "))
NumC = None

while NumB >= 0:
    NumC = NumA % NumB
    print(NumC)

    if NumC == 0:
        print("")
        print(f"The GDC is {NumB}")
        break

    NumA = NumB % NumC
    print(NumA)

    NumB = NumC % NumA
    print(NumB)
