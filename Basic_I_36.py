# Write a Python program to add two objects if both objects are an integer type

print("Python program to add two objects if both objects are an integer type")
# obj1 = input("Object 1: ")
# obj2 = input("Object 2: ")


def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Objects must be integers!"
    else:
        return a + b
    

print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))