#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
user_inp1 = float(input("Please enter a number: "))
user_inp2 = float(input("Enter another number: "))

if user_inp1 == user_inp2:
    print("The numbers entered are equal")
else:
    print("The numbers entered are not equal")