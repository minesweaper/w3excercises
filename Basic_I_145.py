# Write a Python program to test if a variable is a list or tuple or a set

x = ['a', 'b', 'c', 'd']
y = {'a', 'b', 'c', 'd'}
z = ('tuple', False, 3.2, 1)
a = (3, 2, 2, 1)


def check_type(entry):
    if type(entry) is list:
        print('{} is a list'.format(entry))
    elif type(entry) is set:
        print('{} is a set'.format(entry))
    elif type(entry) is tuple:
        print('{} is a tuple'.format(entry))
    else:
        print('{} is a neither a list or a set or a tuple'.format(entry))


check_type(x)
check_type(y)
check_type(z)
check_type(a)
check_type(z)
