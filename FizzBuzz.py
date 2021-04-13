for x in range(1, 101):
    if (((x % 3) == 0) and ((x % 5) == 0)):
        print(x, '\tFizzBuzz')
    elif ((x % 3) == 0):
        print(x, '\tFizz')
    elif ((x % 5) == 0):
        print(x, '\tBuzz')
    else:
        print(x)
