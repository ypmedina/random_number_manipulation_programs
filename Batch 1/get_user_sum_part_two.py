#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
#Create a for function to get 10 user inputs and print the sum of all inputted numbers
user_sum = 0
for i in range(10):
    user_inp = int(input(f"Numbers entered{i+1}"))
    user_sum += user_inp
print(f"{user_sum} is the sum of all numbers entered")