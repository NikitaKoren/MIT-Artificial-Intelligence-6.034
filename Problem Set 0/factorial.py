# python program to find factorial

def factorial(num):
    if num < 0:
        raise "factorial: input must not be negative"
    elif num == 1:
        return num
    else:
        return num * factorial(num - 1)


number = input("Enter a number: ")
print "factorial", factorial(number)
