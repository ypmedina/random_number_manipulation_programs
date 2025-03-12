# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
#Use a for function that goes up to 101 and apply modulus division to remove all numbers ending in zero
for i in range(101):
    if i % 10 != 0:
        print(i)