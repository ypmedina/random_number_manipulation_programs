# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
#Create a for function to get 10 user inputs and print how many odd numbers there are in the inputted numbers
odd_num = 0
for i in range(10):
    user_inp = int(input(f"Numbers entered {i+1}"))
    if user_inp % 2 != 0:
        odd_num += 1

print(f"{odd_num} is the number of odd numbers entered")
