#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
#use a for function to get 10 inputs, figure out how to check for number duplicates
numbers = []
duplicates = []
for i in range(10):
    user_inp = int(input(f"Numbers entered: {i+1} "))

    if user_inp in numbers:
        duplicates.append(user_inp)
    else:
        numbers.append(user_inp)

print(numbers)
print(duplicates)