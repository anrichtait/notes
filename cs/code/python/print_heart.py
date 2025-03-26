def print_grid(grid):
    for row in grid:
        print(''.join(row))


def flip_grid(grid):
    flippedGrid = []
    for col in range(len(grid[0])):
        newRow = []

        for row in range(len(grid)):
            newRow.append(grid[row][col])
        flippedGrid.append(newRow)

    print_grid(flippedGrid)


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print(f"Unformatted grid:\n{grid}")
print('-' * 30)
print("Formateed grid:\n")
print_grid(grid)
print('-' * 30)
print("Flipped grid:\n")
flip_grid(grid)
