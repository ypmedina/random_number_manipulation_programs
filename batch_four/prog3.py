#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
#just reversed a program from batch 3
high = None
while True:
    try:
        user_inp = int(input("Please enter a number "))
        if high is None or user_inp > high:
            high = user_inp
            print(f"The new highest number is {high}")
        else:
            print(f"The entered number is lower than {high}")
    except ValueError:
        print("\nInvalid input, exiting the program now")
        break