# Write a Python program to convert the distance (in feet) to inches, yards, and miles

print("Program to convert the distance (in feet) to inches, yards, and miles")
feet = int(input("Feet: "))

inches = feet * 12
yards = feet / 3
miles = feet / 5280


print("{} feet/foot equals to {} inches".format(feet, inches))
print("{} feet/foot equals to {} yards".format(feet, round(yards, 2)))
print("{} feet/foot equals to {} yards".format(feet, round(miles, 2)))
