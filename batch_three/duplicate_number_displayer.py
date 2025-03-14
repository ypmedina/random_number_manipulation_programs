#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
numbers = []
duplicates = []

for i in range(10):
    user_inp = int(input(f"Numbers entered: {i+1} "))
    numbers.append(user_inp)

for num in numbers:
    if num not in duplicates:
        duplicates.append(num)
        print(num)


