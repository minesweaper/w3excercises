def even_or_odd(number):
    if number%2 == 0:
        print("Number is even")
        return
    else:
        print("Number is odd")
        return


number = int(input("Give a number: "))
even_or_odd(number)
