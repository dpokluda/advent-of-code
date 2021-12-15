class Board:
    def __init__(self, numbers):
        self.numbers = numbers
        self._marked = []
        for _ in numbers:
            line = []
            for __ in numbers:
                line.append(False)
            self._marked.append(list(line))

    def mark(self, number):
        for row in range(0, len(self.numbers)):
            for col in range(0, len(self.numbers[0])):
                if self.numbers[row][col] == number:
                    self._marked[row][col] = True

    def is_winning(self):
        row = self._has_winning_row()
        if row != -1:
            return self.numbers[row]
        col = self._has_winning_column()
        if col != -1:
            return [self.numbers[row][col] for row in range(0, len(self.numbers))]
        return None

    def get_available_numbers(self):
        available = []
        for row in range(0, len(self.numbers)):
            for col in range(0, len(self.numbers[0])):
                if not self._marked[row][col]:
                    available.append(self.numbers[row][col])
        return available

    def _has_winning_row(self):
        for row in range(0, len(self.numbers)):
            is_winning = False
            for col in range(0, len(self.numbers[0])):
                if self._marked[row][col]:
                    is_winning = True
                else:
                    is_winning = False
                    break
            if is_winning:
                # print(f"row:{row}")
                return row
        return -1

    def _has_winning_column(self):
        for col in range(0, len(self.numbers[0])):
            is_winning = False
            for row in range(0, len(self.numbers)):
                if self._marked[row][col]:
                    is_winning = True
                else:
                    is_winning = False
                    break
            if is_winning:
                # print(f"col:{col}")
                return col
        return -1


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    numbers = [int(x) for x in lines[0].split(",")]

    boards = []
    for index in range(1, 1 + (len(lines) - 1) // 6):
        board_numbers = []
        for row in range(1, 6):
            row_numbers = [int(x) for x in lines[1 + (index-1) * 6 + row].lstrip().split()]
            board_numbers.append(list(row_numbers))
        boards += [Board(board_numbers)]

    for number in numbers:
        # print(number)
        for board in boards:
            board.mark(number)
            r = board.is_winning()
            if r is not None:
                a = board.get_available_numbers()
                sum = 0
                for x in a:
                    sum += x
                print(number * sum)
                exit(0)
    raise Exception("No winning board.")
