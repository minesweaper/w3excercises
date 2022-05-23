def sum_of_numbers(a,b,c):
    # a = int(input("Give the 1st number: "))
    # b = int(input("Give the 2nd number: "))
    # c = int(input("Give the 3rd number: "))
    if a == b == c:
        sum = 3 * int(a + b + c)
    else:
        sum = a + b + c
    return sum


print(sum_of_numbers(1,1,2))
