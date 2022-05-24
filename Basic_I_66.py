# Write a Python program to calculate body mass index

weight = int(input("Weight: "))
height = int(input("Height: "))
BMI = weight / ((height/100)**2)

print(BMI)