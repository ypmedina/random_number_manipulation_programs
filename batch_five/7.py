"""Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
Example:
Input: We will weather the weather whatever the weather whether we like it or not
Output: 14"""

user_input = input("Please enter a sentence: ")
word_amount = len(user_input.split())

print(word_amount)
