# Write a Python program to compute the future value of a specified principal amount,
# rate of interest, and a number of years.
#
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

def future_value(amt, int, y):
    fv = amt * (1 + (int/100)) ** y
    return print(round(fv,2))


future_value(10000, 3.5, 7)
