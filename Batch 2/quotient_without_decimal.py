#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
user_inp1 = float(input("Please enter a number: "))
user_inp2 = float(input("Enter another number: "))

inp_division = user_inp1 // user_inp2
print(f"{inp_division} is the quotient of the two numbers without the decimal")