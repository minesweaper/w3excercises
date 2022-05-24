# Write a Python program to compute the distance between the points

def distance_between_points(x1, y1, x2, y2):
    distance_squared = (x1 - x2)**2 + (y1 - y2)**2
    distance = distance_squared**(1/2)
    return print(distance)


x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

distance_between_points(x1, y1, x2, y2)