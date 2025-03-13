user_sum = 0
for i in range(10):
    user_inp = int(input(f"Numbers entered {i+1}: "))
    user_sum += user_inp
print(f"{user_sum} is the sum of all numbers entered")