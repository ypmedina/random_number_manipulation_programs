"""
Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
Example:
Input: 143
Output: 000143
"""

user_input = int(input("Please enter a whole number between 0-1000: "))
num_format = f"{user_input:06d}"

if 0 <= user_input <= 1000:
    print(num_format)

else:
     print("That is not a valid input, please input numbers between 0 and 1000")




