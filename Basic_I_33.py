# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
print("Give 3 integers to calculate a sum. If 2 numbers are equal the sum will equal 0")
number1 = int(input("Input your first integer: "))
number2 = int(input("Input your second integer: "))
number3 = int(input("Input your third integer: "))

def sum_of_integers(number1, number2, number3):
    if number1 == number2 or number1 == number3 or number2 == number3:
        sum_of_numbers = 0
    else:
        sum_of_numbers = number1 + number2 + number3
    return sum_of_numbers


print(sum_of_integers(number1,number2,number3))