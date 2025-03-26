def print_table(list):
    for line in range(len(list[0])):
        for col in range(len(list)):
            print(list[col][line].ljust(10, ' '), end='')
        print()


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    print_table(tableData)


main()
