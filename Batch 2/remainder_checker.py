#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
user_inp1 = float(input("Please enter a number: "))
user_inp2 = float(input("Enter another number: "))

inp_remainder = user_inp1 % user_inp2
print(f"{inp_remainder} is the remainder when the first number is divided by the second number")