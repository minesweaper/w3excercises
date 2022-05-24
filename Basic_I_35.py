# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

def basic35(x,y):
    if x == y or abs(x-y) == 5:
        return True
    else:
        return False


print(basic35(4,4))
print(basic35(10,5))
print(basic35(5,10))
print(basic35(5,7))


