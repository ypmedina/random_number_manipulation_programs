#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
#use a while loop, make a list, get the len of the list and the sum of the values in the list and then divide them
#use a def function to make the average program
numbers = []

while True:
    try:
        user_inp = int(input("Enter a number: "))
        numbers.append(user_inp)

        avg = sum(numbers) / len(numbers)
    except ValueError:
        print(avg)
        break