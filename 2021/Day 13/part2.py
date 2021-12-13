def fold_board(board, axis, value):
    if axis == 'y':
        max = len(board)
        for index in range(0, value):
            for col in range(0, len(board[0])):
                # print(f"[{value-(max - value) + index + 1}][{col}] <- [{max - index - 1}][{col}]")
                board[value-(max - value) + index + 1][col] += board[max - index - 1][col]
        for row in range(value, max):
            board.pop()
    elif axis == 'x':
        max = len(board[0])
        for row in range(0, len(board)):
            for index in range(0, value):
                # print(f"[{row}][{value-(max - value) + index + 1}] <- [{row}][{max - index - 1}]")
                board[row][value-(max - value) + index + 1] += board[row][max - index - 1]
            for col in range(value, max):
                board[row].pop()


def create_board(points):
    board = []
    for row in range(0, 11):
        line = []
        for col in range(0, 11):
            line.append(0)
        board.append(line)
    for point in points:
        board[point[1]][point[0]] = 1
    return board


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    points = []
    folds = []
    max_x = 0
    max_y = 0
    for line in lines:
        if line.startswith("fold along"):
            fold = line.split(" ")[2].split("=")
            folds.append([fold[0], int(fold[1])])
        elif line == '':
            continue
        else:
            point = [int(x) for x in line.split(",")]
            if point[0] > max_x:
                max_x = point[0]
            if point[1] > max_y:
                max_y = point[1]
            points.append(point)

    # board = create_board([[0,0], [10,10]])
    # print(board)
    # fold_board(board, 'y', 5)
    # print(board)

    board = []
    for row in range(0, max_y+1):
        row = []
        for col in range(0, max_x+1):
            row.append(0)
        board.append(row)
    for point in points:
        board[point[1]][point[0]] = 1

    for fold in folds:
        fold_board(board, fold[0], fold[1])

    for row in range(0, len(board)):
        line = ""
        for col in range(0, len(board[0])):
            if board[row][col] > 0:
                line += "*"
            else:
                line += " "
        print(line)
