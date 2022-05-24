# Write a Python program to calculate the hypotenuse of a right angled triangle.

print("Program to calculate the hypotenuse of a right angled triangle")
a = float(input("a: "))
b = float(input("b: "))

def hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** (1/2)
    return print(c)


hypotenuse(a, b)