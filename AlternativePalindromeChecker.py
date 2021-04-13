from collections import deque
import re


def checker(word):
    palChecker = deque()

    word = re.sub(' ', '', word)

    for x in word:
        palChecker.append(x.upper())

    stillTrue = True

    while len(palChecker) > 1 and stillTrue:
        firstChar = palChecker.popleft()
        lastChar = palChecker.pop()
        if not(firstChar == lastChar):
            stillTrue = False
    return stillTrue


words = ['Taco Cat', 'Brian', 'Bob', 'Billy']

for x in words:
    if (checker(x)):
        print(x, 'is a Palidrome')
    else:
        print(x, 'is not a Palidrome')
