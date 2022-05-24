# Write a Python program to sum of the first n positive integers

def sum_of_n_integers(n):
    sum_of_integers = 0
    for i in range(0,n+1):
        sum_of_integers += i
    return sum_of_integers


print(sum_of_n_integers(0))
print(sum_of_n_integers(1))
print(sum_of_n_integers(2))
print(sum_of_n_integers(3))
print(sum_of_n_integers(4))
print(sum_of_n_integers(5))