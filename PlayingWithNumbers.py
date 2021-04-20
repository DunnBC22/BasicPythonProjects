import math
'''
Take a number that is inputted and split it into 2s and 3s (maximize the number of
3s first). Take those numbers and multiply them together to get the maximum
product of the values.
'''


def defineNumber():
    number = input('Please enter a number ')
    try:
        (isinstance(type(number), int))
    except ValueError:
        print('Please try again. Only integer values are accepted.')
        number = input("Please enter a number ")
    else:
        number = int(number)
        return number


def division(total: int, number: int, modVal: int):
    remainder = number % modVal
    print('remainder:', remainder)
    instances = math.floor(number / modVal)
    print('instances:', instances)
    internal_total = modVal**instances
    print('total:', total)
    if (modVal == 3):
        division(internal_total, remainder, 2)
    else:
        finalTotal = total * internal_total
        print('The sum of the values is', finalTotal)
        quit()


if __name__ == '__main__':
    num = defineNumber()
    division(0, num, 3)
    quit()
