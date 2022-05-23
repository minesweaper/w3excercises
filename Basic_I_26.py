def histogram(x, y):
    for n in y:
        output = ''
        times = n
        while (times > 0):
            output += str(x)
            times -= 1
        print(output)


histogram('@', [7,2,5,6])
