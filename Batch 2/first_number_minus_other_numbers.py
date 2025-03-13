#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
total = 0
for i in range(10):
    user_inp = int(input(f"Number {i+1}: "))
    total -= user_inp
print(f"{total} is the first number minus the remaining numbers")