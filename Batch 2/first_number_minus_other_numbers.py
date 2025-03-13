#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
total = []
for i in range(10):
    user_inp = float(input(f"Number {i+1}: "))
    total.append(user_inp)
    difference = total[0] - sum(total[1:])
print(f"{difference} is the first number minus the remaining numbers")