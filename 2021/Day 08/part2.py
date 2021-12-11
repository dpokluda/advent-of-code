letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def normalize(digits):
    sorted = list(digits)
    sorted.sort()
    return ''.join(sorted)


def calculate_wiring(digits):
    list_digits = [list(x) for x in digits]
    missing_pieces = {x: 0 for x in letters}
    pieces_in_1 = []
    for digit in list_digits:
        for letter in letters:
            if letter not in digit:
                missing_pieces[letter] += 1
        if len(digit) == 2:
            pieces_in_1 += digit

    # print(missing_pieces)
    # print(f"pieces_in_1: {pieces_in_1}")
    missing_piece_once = ''
    missing_piece_six = ''
    for index, (piece, count) in enumerate(missing_pieces.items()):
        if count == 1:
            missing_piece_once = piece
        if count == 6:
            missing_piece_six = piece
    # print(f"missing_piece_once: {missing_piece_once}")
    # print(f"missing_piece_six: {missing_piece_six}")

    wiring = {}
    stage = 0
    while len(digits) > 0:
        stage += 1
        digits_to_process = []
        for digit in digits:
            digits_to_process.append(digit)
        for digit in digits_to_process:
            if len(digit) == 2:
                wiring[digit] = 1
                digits.remove(digit)
            if len(digit) == 3:
                wiring[digit] = 7
                digits.remove(digit)
            if len(digit) == 4:
                wiring[digit] = 4
                digits.remove(digit)
            if len(digit) == 7:
                wiring[digit] = 8
                digits.remove(digit)

            if len(digit) == 5:
                if stage == 1 and pieces_in_1[0] in digit and pieces_in_1[1] in digit:
                    wiring[digit] = 3
                    digits.remove(digit)
                elif stage == 2 and missing_piece_once not in digit:
                    wiring[digit] = 2
                    digits.remove(digit)
                elif stage > 2:
                    wiring[digit] = 5
                    digits.remove(digit)
            if len(digit) == 6:
                if stage == 1 and missing_piece_six not in digit:
                    wiring[digit] = 9
                    digits.remove(digit)
                elif stage == 2 and pieces_in_1[0] in digit and pieces_in_1[1] in digit:
                    wiring[digit] = 0
                    digits.remove(digit)
                elif stage > 2:
                    wiring[digit] = 6
                    digits.remove(digit)
    return wiring


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    sum = 0
    for line in lines:
        segments = line.split(" | ")
        all_digits = [normalize(x) for x in segments[0].split(" ")]
        # print(all_digits)
        wiring = calculate_wiring(all_digits)
        # print(wiring)
        digits = [normalize(x) for x in segments[1].split(" ")]
        number = 0
        for digit in digits:
            number = number * 10 + wiring.get(digit)
        print(number)
        sum += number
    print(sum)
