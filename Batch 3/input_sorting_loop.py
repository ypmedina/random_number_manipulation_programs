#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid.
#Display the number from lowest to highest. Clue: sort() function

#make a list to store all numbers, use a while loop with try and except functions, put the user input
#in the list and use sort function

#well that was easier than expected
numbers =[]
while True:
    try:
        user_inp = int(input("Enter a number: "))
        numbers.append(user_inp)
        numbers.sort()
        print(numbers)

    except ValueError:
        print("\nThe input is invalid, exiting program now")
        break