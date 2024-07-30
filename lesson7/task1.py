def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
a = float(input("number 1: "))
b = float(input("number 2: "))
max_num = find_max(a, b)
print(f"the number that is greater: {max_num}")



   