even_num = 0
for i in range(10):
    user_inp = int(input(f"Number {i+1}: "))
    if user_inp % 2 == 0:
        even_num += 1
print(f"There are {even_num} even numbers")