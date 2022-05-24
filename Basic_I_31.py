# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

print("Compute the greatest common divisor of two positive integers")
first_integer = int(input("First integer: "))
second_integer = int(input("Second integer: "))

set_divisor1 = []
set_divisor2 = []

for x in range(1, first_integer+1):
    if x == 0:
        pass
    elif first_integer % x == 0:
        set_divisor1.append(x)

for y in range(1, second_integer+1):
    if y == 0:
        pass
    elif second_integer % y == 0:
        set_divisor2.append(y)

print(set_divisor1)
print(set_divisor2)

gcd = []
for x in set_divisor1:
    if x in set_divisor2:
        gcd.append(x)
print(max(gcd))


# def gcd(x, y):
#     gcd = 1
#     if x % y == 0:
#         return y
#     for k in range(int(y / 2), 0, -1):
#         if x % k == 0 and y % k == 0:
#             gcd = k
#             break
#     return gcd
# print("GCD of 40 & 20 =",gcd(12, 17))
# print("GCD of 4 & 8 =",gcd(4, 6))
# print("GCD of 336 & 360 =",gcd(336, 360))