# Write a Python program to swap two variables

x = input("x: ")
y = input("y: ")

# temp = y
# y = x
# x = temp

x, y = y, x

print("x = {} and y = {}".format(x,y))