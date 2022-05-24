# Write a Python program to display your details like name, age, address in three different lines

def print_personal_data():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))


print_personal_data()