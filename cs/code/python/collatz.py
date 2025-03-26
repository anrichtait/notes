import sys


def collatz_sequence(num):
    if num % 2 == 0:
        evenOut = num // 2
        print(evenOut)
        return evenOut
    elif num % 2 == 1:
        oddOut = 3 * num + 1
        print(oddOut)
        return oddOut


while True:
    inputNum = input("Enter a number: ")
    try:
        passNum = int(inputNum)
        break
    except ValueError:
        print("That's not a valid integer!")


checker = collatz_sequence(passNum)
while checker != 1:
    checker = collatz_sequence(checker)

sys.exit()
