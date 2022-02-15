# print(10 % 3)
#
# if (num1 % num2) == 0:
#     #do this, eg add those numbers to a list
# else:
#     #do that, eg print or ignore

# write a program that will print the following multi-line string:
# ' '' '''
# ' '' '''
# ' '' '''

# for i in range(3):
#     print("' '' '''")

for x in range(1000 + 1):
   if x > 1:
       for n in range(2, x):
           if (x % n) == 0:
               break
       else:
           print(x)
