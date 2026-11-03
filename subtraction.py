# without built-in function

a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

i = len(a) - 1
j = len(b) - 1

borrow = 0
result = ""

while i >= 0:
    x = int(a[i]) - borrow
    y = int(b[j]) if j >= 0 else 0

    if x < y:
        x = x + 2
        borrow = 1
    else:
        borrow = 0

    result = str(x - y) + result

    i -= 1
    j -= 1

print("Subtraction:", result.lstrip('0') or '0')

# with built-in function

a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

num1 = int(a, 2)
num2 = int(b, 2)

result = num1 - num2

print("Subtraction of binary numbers:", bin(result)[2:])
