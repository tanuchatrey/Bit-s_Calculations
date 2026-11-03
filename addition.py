a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

num1 = int(a, 2)
num2 = int(b, 2)

sum = num1 + num2

result = bin(sum)[2:]

print("Addition of binary numbers:", result)
