#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
#reversed a program from batch 3
numbers =[]
while True:
    try:
        user_inp = int(input("Enter a number: "))
        numbers.append(user_inp)
        numbers.sort(reverse=True)
        print(numbers)

    except ValueError:
        print("\nThe input is invalid, exiting program now")
        break