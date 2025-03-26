print("Age:")
userAge = input()
userAge = int(userAge)

if userAge / 1 != userAge:
    print("Input Error")
else:
    print(input, end='')
    print()
    if userAge < 16:
        print("You are too young for this application.")
        print()
    elif userAge >= 15:
        print("Please proceed.")
        print()
    else:
        print("Input error!")
