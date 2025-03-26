import random


def flip(numFlips):
    flip = 0
    history = []
    numFlips = int(numFlips)

    for i in range(numFlips):
        flip = random.randint(1, 2)
        history.append(flip)

    return history


def check_streaks(history):
    lastFlip = 0
    currentStreak = 0
    totalStreaks = 0

    for currentFlip in history:
        if lastFlip == currentFlip:
            currentStreak += 1
            if currentStreak == 6:
                totalStreaks += 1
        elif lastFlip != currentFlip:
            currentStreak = 1
        lastFlip = currentFlip
    return totalStreaks


history = flip(100)
print('-' * 30)
print(history)
print('-' * 30)
totalStreaks = check_streaks(history)
print(totalStreaks)
