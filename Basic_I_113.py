#  Write a Python program to input a number, if it is not a number generates an error message.
while True:
    try:
        number = int(input("Input: "))
        print("Is a number")
    except ValueError:
        print("Not a number")
        break
