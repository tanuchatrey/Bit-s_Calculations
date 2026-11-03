# with built-in function

a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

num1 = int(a, 2)
num2 = int(b, 2)

result = num1 * num2

print("Multiplication of binary numbers:", bin(result)[2:])

# without built-in function

a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

result = 0
power = 0

for digit in reversed(b):
    if digit == '1':
        result += int(a, 2) << power
    power += 1

# Convert decimal result to binary
binary = ""

if result == 0:
    binary = "0"
else:
    while result > 0:
        binary = str(result % 2) + binary
        result //= 2

print("Multiplication:", binary)
