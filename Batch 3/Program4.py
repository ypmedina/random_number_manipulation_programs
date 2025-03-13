#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
#Use the while loop again, check for the lowest inputted number and make that value the set number so that
#It will not read a higher number and call it the lowest

while True:
    try:
        user_inp = int(input("Please enter a number "))

        
    except ValueError:
        break




