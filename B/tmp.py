board = {
    "A1": 'A',
    "A2": 'B',
    "A3": 'c',
    "B1": 'd',
    "B2": 'e',
    "B3": 'f',
    "C1": 'g',
    "C2": 'h',
    "C3": 'i',
}

for let in "ABC":
    # print(let)
    for num in "123":
        # print(let,num)
        pos = let + num
        print(board[pos], end='')
    print()
    