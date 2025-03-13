total = []
for i in range(10):
    user_inp = float(input(f"Number {i+1}: "))
    total.append(user_inp)
    difference = total[0] - sum(total[1:])
print(f"{difference} is the first number minus the remaining numbers")