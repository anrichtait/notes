def user_moves(player):
    i = 0
    while i < 9:
        if player == 1:
            move = input("Enter a move: ")
            theBoard[move] = 'x'
            print_board()
            player += 1
        elif player == 2:
            move = input("Enter a move: ")
            theBoard[move] = 'o'
            print_board()
            player -= 1


def print_board():
    print(f"{theBoard['tl']} | {theBoard['tm']} | {theBoard['tr']}")
    print(splitter)
    print(f"{theBoard['ml']} | {theBoard['mm']} | {theBoard['mr']}")
    print(splitter)
    print(f"{theBoard['ll']} | {theBoard['lm']} | {theBoard['lr']}")


splitter = '--+---+--'

theBoard = {'tl': ' ', 'tm': ' ', 'tr': ' ',
            'ml': ' ', 'mm': ' ', 'mr': ' ',
            'll': ' ', 'lm': ' ', 'lr': ' '}


def main():
    moveTracker = 1

    print_board()
    user_moves(moveTracker)
    print_board()
    print()


main()
