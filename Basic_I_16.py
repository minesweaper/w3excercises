# number = int(input("Number: "))
# if number <= 17:
#     print(f"Difference is equal to: {17-number}")
# else:
#     print(f"Double the absolute difference is equal to {2*(number-17)}")

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2


print(difference(22))
print(difference(14))
