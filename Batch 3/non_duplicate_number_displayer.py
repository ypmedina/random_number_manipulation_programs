#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
#use a for function to get 10 inputs, figure out how to check for number duplicates
numbers = []
non_dupe= []
for i in range(10):
    user_inp = int(input(f"Numbers entered: {i+1} "))
    numbers.append(user_inp)

if numbers.count():
    non_dupe.append(numbers)

print(non_dupe)
