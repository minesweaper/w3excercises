def larger_string(str, n):
    result = ""
    for i in range(n):
        result += str
        result += ". "
    return result


print(larger_string('My string', 10))