#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
user_inp1 = float(input("Please enter a number: "))
user_inp2 = float(input("Enter another number: "))

if user_inp1 < user_inp2:
    print(f"{user_inp1} is the smaller number")
else:
    print(f"{user_inp2} is the smaller number")