#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
#Use a 'for' function for the user input, store the inputs in a list and display all the duplicate numbers in that list
#using another 'for' function

numbers = []
duplicates = []
for i in range(10):
    user_inp = int(input(f"Numbers entered {i+1}: "))
    numbers.append(user_inp)

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)



