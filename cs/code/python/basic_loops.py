def w_loop(value):
    i = 0
    while i < value:
        print("While Iteration: ", i, end='')
        print()
        i = i + 1


def f_loop(value):
    i = 0
    for i in range(value):
        print("For Iteration: ", i, end='')
        print()
        i = i + 1


def b_loop(value):
    i = 0
    while True:
        print("i Is now equal to:", value)
        i = i + 1
        if i == value:
            break
    print("i Is now equal to:", value)


print("Type a number: \n")
value = input()
value = int(value)
f_loop(value)
w_loop(value)
b_loop(value)
