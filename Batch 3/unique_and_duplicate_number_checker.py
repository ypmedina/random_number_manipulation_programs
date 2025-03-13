#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
#Make a "while" statement and use "try" and "except" functions to catch invalid inputs
#For the unique and dupes, just use the same technique as the previous programs

numbers = []
while True:
    try:
        user_inp = int(input("\nPlease enter a number: "))

        if user_inp in numbers:
            print("This is a duplicate number")
        else:
            print("This is a unique number")
            numbers.append(user_inp)

    except ValueError:
        print("\nInvalid input, now exiting the program")
        break