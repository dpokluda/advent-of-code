digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def is_digit(line, index):
    result = False
    while line[index] in digits:
        result = True
        index += 1
    return result, index


def is_char(line, index, char):
    result = False
    if line[index] == char:
        result = True
    return result


def is_valid(line):
    level = 0
    for index in range(len(line)):
        if is_char(line, index, '['):
            level += 1
        elif is_char(line, index, ']'):
            level -= 1
    return level == 0


def is_simple_number(line, index):
    next_index = index
    if is_char(line, next_index, '['):
        next_index += 1
        result, next_index = is_digit(line, next_index)
        if result and is_char(line, next_index, ','):
            next_index += 1
            result, next_index = is_digit(line, next_index)
            if result and is_char(line, next_index, ']'):
                next_index += 1
                return True, next_index
    return False, -1


def make_number(line, index):
    if line[index] == '[':
        number = []
        (n, index) = make_number(line, index + 1)
        number.append(n)
        (n, index) = make_number(line, index)
        number.append(n)
    else:
        previous_index = index
        while line[index] not in [',', ']']:
            index = index + 1
        number = int(line[previous_index:index])
    return number, index + 1


def reduce_number(line):
    do_repeat = True
    while do_repeat:
        if is_valid(line) is False:
            print('invalid: ', line)

        do_repeat = False
        new_line = explode_number(line)
        if new_line is not None:
            do_repeat = True
            line = new_line
            # print('explode:', line)
            continue

        new_line = split_number(line)
        if new_line is not None:
            do_repeat = True
            line = new_line
            # print('split:', line)

    # print('final:', line)
    return line


def explode_number(line):
    left_expand_index = None
    right_expand_index = None
    expand_index_from = None
    expand_index_to = None
    level = 0
    index = 0
    while index < len(line):
        result, next_index = is_simple_number(line, index)
        if result and level >= 4 and expand_index_from is None:
            expand_index_from = index
            expand_index_to = next_index
            index = next_index-1
        elif is_char(line, index, '['):
            level += 1
        elif is_char(line, index, ']'):
            level -= 1
        else:
            result, next_index = is_digit(line, index)
            if result:
                if expand_index_from is None:
                    left_expand_index = index
                if expand_index_to is not None and expand_index_to < index and right_expand_index is None:
                    right_expand_index = index
                index = next_index-1
        index += 1

    if expand_index_from is None:
        return None

    # print(line)
    # minus = 0
    # if left_expand_index is not None:
    #     print(' ' * left_expand_index, end='')
    #     print('l', end='')
    #     minus = left_expand_index + 1
    # print(' ' * (expand_index_from - minus), end='')
    # print('f', end='')
    # print(' ' * (expand_index_to - expand_index_from - 1), end='')
    # print('t', end='')
    # minus = expand_index_to + 1
    # if right_expand_index is not None:
    #     print(' ' * (right_expand_index - minus), end='')
    #     print('r', end='')
    #     minus = right_expand_index + 1
    # print(' ' * (len(line) - minus))

    new_line = ''
    _, expand_index_left_to = is_digit(line, expand_index_from + 1)
    _, expand_index_right_to = is_digit(line, expand_index_left_to + 1)
    if left_expand_index is not None:
        _, left_expand_index_to = is_digit(line, left_expand_index)
        left_expand_number = int(line[left_expand_index:left_expand_index_to])
        left_number = int(line[expand_index_from+1:expand_index_left_to])
        new_line = line[:left_expand_index] + str(left_expand_number + left_number) + line[left_expand_index_to:expand_index_from]
    else:
        new_line = line[:expand_index_from]

    new_line += '0'

    if right_expand_index is None:
        new_line += line[expand_index_to:]
    else:
        _, right_expand_index_to = is_digit(line, right_expand_index)
        right_expand_number = int(line[right_expand_index:right_expand_index_to])
        right_number = int(line[expand_index_left_to+1:expand_index_right_to])
        new_line += line[expand_index_to:right_expand_index] + str(right_number + right_expand_number) + line[right_expand_index_to:]
    # print(new_line)

    return new_line


def split_number(line):
    index = 0
    while index < len(line):
        result, index_to = is_digit(line, index)
        if result and index_to > index+1:
            number = int(line[index:index_to])
            left = number // 2
            right = number // 2 + (0 if number % 2 == 0 else 1)
            new_line = line[:index] + '[' + str(left) + ',' + str(right) + ']' + line[index_to:]
            return new_line
        index += 1
    return None


def calculate_magnitute(number):
    left, right = number
    if type(left) is list:
        left = calculate_magnitute(left)
    if type(right) is list:
        right = calculate_magnitute(right)
    return left*3 + right*2


def assert_equal(expected, actual):
    if expected == actual:
        print(f"Pass: {actual}")
    else:
        print(f"Fail: {actual} != {expected}")


def run():
    # assert_equal('[[[[0,9],2],3],4]', explode_number('[[[[[9,8],1],2],3],4]'))
    # assert_equal('[7,[6,[5,[7,0]]]]', explode_number('[7,[6,[5,[4,[3,2]]]]]'))
    # assert_equal('[[6,[5,[7,0]]],3]', explode_number('[[6,[5,[4,[3,2]]]],1]'))
    # assert_equal('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', explode_number('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'))
    # assert_equal('[[3,[2,[8,0]]],[9,[5,[7,0]]]]', explode_number('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'))
    #
    # assert_equal('[1,[2,[3,[9,0],[9,4]]]]', explode_number('[1,[2,[3,[4,[5,5]],[4,4]]]]'))
    # assert_equal('[[[[4,9],[0,9],3],2],1]', explode_number('[[[[4,4],[[5,5],4],3],2],1]'))

    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    max_magnitute = 0
    for first in range(len(lines)):
        print(first)
        for second in range(len(lines)):
            if second == first:
                continue
            if lines[first] is None or \
               lines[second] is None:
                continue

            line = '[' + lines[first] + ',' + lines[second] + ']'
            line = reduce_number(line)
            # print(line)
            number = make_number(line, 0)
            magnitute = calculate_magnitute(number[0])
            if magnitute > max_magnitute:
                max_magnitute = magnitute

    print(max_magnitute)