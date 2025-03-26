import random

wins, draws, losses = 0, 0, 0


def kill_game():
    print("Thanks for playing!")
    exit()


def calc_winner(uMove, aiMove):
    global wins
    global draws
    global losses

    if uMove == aiMove:
        print("Draw!")
        draws += 1
        return 0
    elif (uMove == 1 and aiMove == 3) or (uMove == 2 and aiMove == 1) or (uMove == 3 and aiMove == 2):
        print("You win!")
        wins += 1
        return 1
    else:
        print("You lose!")
        losses += 1
        return 0


def print_score():
    print("---------------------")
    print(wins, "Wins,", losses, "Losses,", draws, "Draws,")
    print("---------------------")


def startup_screen():
    global wins, losses, draws
    print()
    print("ROCK, PAPER, SCISSORS")
    print("---------------------")
    print(wins, "Wins,", losses, "Losses,", draws, "Draws,")
    print("---------------------")


def move_prompt():
    print("Enter your move: (r)ock (p)aper (s)cissors or q(uit)")
    userMove = input()
    if userMove == 'r':
        return 1
    elif userMove == 'p':
        return 2
    elif userMove == 's':
        return 3
    else:
        kill_game()


def print_versus(uMove, aiMove):
    if uMove == 1:
        uMove = "Rock"
    elif uMove == 2:
        uMove = "Paper"
    elif uMove == 3:
        uMove = "Scissors"

    if aiMove == 1:
        aiMove = "Rock"
    elif aiMove == 2:
        aiMove = "Paper"
    elif aiMove == 3:
        aiMove = "Scissors"

    print(uMove, "VERSUS", aiMove)
    print()


def ai_move():
    random_number = random.randint(1, 3)
    if random_number == 1:
        return 1
    elif random_number == 2:
        return 2
    elif random_number == 3:
        return 3


startup_screen()
userMove = move_prompt()
print("userMove: ", userMove)
while userMove == 1 or 2 or 3:
    aiMove = ai_move()
    print("aiMove: ", aiMove)
    print_versus(userMove, aiMove)
    calc_winner(userMove, aiMove)
    print_score()
    move_prompt()
