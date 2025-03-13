#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
#Use the while loop again, check for the lowest inputted number and make that value the set number so that
#It will not read a higher number and call it the lowest
lowest = None
while True:
    try:
        user_inp = int(input("Please enter a number "))
        if lowest == None or user_inp < lowest:
            lowest = user_inp
            print(f"The new lowest number is {lowest}")
        else:
            print(f"The entered number is higher than {lowest}")
    except ValueError:
        print("\nInvalid input, exiting the program now")
        break




