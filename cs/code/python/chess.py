def check_valid_pieces(board):
    pieceCounts = {
            'wPawn': 0,
            'bPawn': 0,
            'wKing': 0,
            'bKing': 0,
            'wQueen': 0,
            'bQueen': 0,
            'wHorse': 0,
            'bHorse': 0,
            'wBishop': 0,
            'bBishop': 0,
            'wCastle': 0,
            'bCastle': 0
            }
    for piece in board.values():
        if piece in pieceCounts:
            pieceCounts[piece] += 1

    # check rules
    valid = True
    if pieceCounts['wKing'] != 1 or pieceCounts['bKing'] != 1:
        valid = False
        print(f"There are too many kings")
    elif pieceCounts['wQueen'] != 1 or pieceCounts['bQueen'] != 1:
        valid = False
        print(f"There are too many queens")
    elif pieceCounts['wBishop'] != 2 or pieceCounts['bBishop'] != 2:
        valid = False
        print(f"There are too many Bishops")
    elif pieceCounts['wCastle'] != 2 or pieceCounts['bCastle'] != 2:
        valid = False
        print(f"There are too many Castles")
    elif pieceCounts['wHorse'] != 2 or pieceCounts['bHorse'] != 2:
        valid = False
        print(f"There are too many Horses")
    elif pieceCounts['wPawn'] != 8 or pieceCounts['bPawn'] != 8:
        valid = False
        print(f"There are too many pawns: {pieceCounts['wPawn']['bPawn']}")
    else:
        valid = True
        print("Valid!")
    return valid



def declare_board():
    board = {}
    columns = 'abcdefgh'
    rows = range(1, 9)
    for row in rows:
        for col in columns:
            # white pieces
            if row == 2:
                value = 'wPawn'
            elif row == 1 and (col == 'a' or col == 'h'):
                value = 'wCastle'
            elif row == 1 and (col == 'b' or col == 'g'):
                value = 'wHorse'
            elif row == 1 and (col == 'c' or col == 'f'):
                value = 'wBishop'
            elif row == 1 and col == 'd':
                value = 'wKing'
            elif row == 1 and col == 'e':
                value = 'wQueen'
            # black pieces
            elif row == 7:
                value = 'bPawn'
            elif row == 8 and (col == 'a' or col == 'h'):
                value = 'bCastle'
            elif row == 8 and (col == 'b' or col == 'g'):
                value = 'bHorse'
            elif row == 8 and (col == 'c' or col == 'f'):
                value = 'bBishop'
            elif row == 8 and col == 'e':
                value = 'bKing'
            elif row == 8 and col == 'd':
                value = 'bQueen'
            else:
                value = ''
            square = f"{col}{row}"
            board[square] = value

    return board


def print_board(board):
    columns = 'abcdefgh'
    rows = range(8, 0, -1)
    for row in rows:
        for col in columns:
            square = f"{col}{row}"
            value = board.get(square, '')
            if value == '':
                print(f"{square:^10}|", end=' ')
            else:
                print(f"{value:^10}|", end=' ')
        print()
        splitter()


def splitter():
    print("-" * 95)


board = declare_board()
print_board(board)
check_valid_pieces(board)
