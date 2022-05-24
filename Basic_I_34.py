# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
print("Give 2 integers to calculate a sum. If the sum is between 15 to 20 it will return 20")
number1 = int(input("Input your first integer: "))
number2 = int(input("Input your second integer: "))


def sum_of_integers2(x, y):
    sum_of_numbers = x + y
    if 20 >= sum_of_numbers >= 15:
        sum_of_numbers = 20
    return sum_of_numbers


print(sum_of_integers2(number1,number2))