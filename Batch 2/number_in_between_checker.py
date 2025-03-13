#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
user_inp1 = int(input("Please enter a number: "))
user_inp2 = int(input("Enter another number: "))

if user_inp1 > user_inp2:
    user_inp1, user_inp2 = user_inp2, user_inp1

for i in range (user_inp1+1, user_inp2, 1):
    print(i)