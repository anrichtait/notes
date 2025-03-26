gridName = ""


def print_grid(grid, nameOfGrid):
    print_splitter(30)
    print(f"{nameOfGrid}:")
    for row in grid:
        print(''.join(row))
    print_splitter(30)


def rotate_grid_90(grid):
    rotatedGrid = []
    for col in range(len(grid[0])):
        newRow = []
        for row in range(len(grid)):
            newRow.append(grid[col][row])
        rotatedGrid.append(newRow)

    return rotatedGrid


def reflect_grid_diagonal(grid):
    pass


def print_splitter(length):
    print('-' * length)


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

gridName = "Original Grid"
print_grid(grid, gridName)

gridName = "Rotated Grid 90"
rotatedGrid = rotate_grid_90(grid)
print_grid()
