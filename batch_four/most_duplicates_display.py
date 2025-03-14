#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the number of duplicate.
#use a while loop and append inputs to a list,

numbers = []
while True:
    try:
        user_inp = int(input("Enter a number: "))
        numbers.append(user_inp)
    except ValueError:
        break

if numbers:
    common_value = numbers[0]
    max_count = 0

    for num in numbers:
        count = numbers.count(num)
        if count > max_count:
            max_count = count
            common_value = num
    print(common_value, max_count)

else:
    print("none")






