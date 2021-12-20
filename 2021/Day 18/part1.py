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
        while do_repeat:
            print('explode:', line)
            do_repeat = False
            new_line = explode_number(line)
            if new_line is not None:
                do_repeat = True
                line = new_line
        do_repeat = True
        while do_repeat:
            print('split:', line)
            do_repeat = False
            new_line = split_number(line)
            if new_line is not None:
                do_repeat = True
                line = new_line
        print('final:', line)
    return line


def explode_number(line):
    left_expand_index = None
    right_expand_index = None
    expand_index_from = None
    expand_index_to = None
    level = 0
    for index in range(len(line)):
        if line[index] == '[' and \
                line[index + 1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and \
                line[index + 2] == ',' and \
                line[index + 3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and \
                line[index + 4] == ']' and \
                level >= 4 and \
                expand_index_from is None:
            expand_index_from = index
            expand_index_to = index + 4
        elif line[index] == '[':
            level += 1
        elif line[index] == ']':
            level -= 1
        elif line[index] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if expand_index_from is None:
                left_expand_index = index
            if expand_index_to is not None and expand_index_to < index and right_expand_index is None:
                right_expand_index = index

    if expand_index_from is None:
        return None

    new_line = ''
    if left_expand_index is not None:
        left_number = int(line[left_expand_index:left_expand_index+1])
        a = line[:left_expand_index]
        e = int(line[expand_index_from + 1:expand_index_from + 2])
        d = left_number + int(line[expand_index_from + 1:expand_index_from + 2])
        b = str(left_number + int(line[expand_index_from + 1:expand_index_from + 2]))
        c = line[left_expand_index + 1:expand_index_from]
        new_line = line[:left_expand_index] + str(left_number + int(line[expand_index_from+1:expand_index_from+2])) + line[left_expand_index+1:expand_index_from]
    if left_expand_index is None:
        new_line = line[:expand_index_from]
    if right_expand_index is None:
        new_line += '0' + line[expand_index_to+1:]
    if right_expand_index is not None:
        right_number = int(line[expand_index_from+3:expand_index_from+4])
        new_line += '0' + line[expand_index_to+1:right_expand_index] + str(right_number + int(line[right_expand_index:right_expand_index+1])) + line[right_expand_index+1:]

    return new_line


def split_number(line):
    for index in range(len(line)):
        if line[index] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and \
                line[index + 1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            number = int(line[index:index+2])
            left = number // 2
            right = number // 2 + (1 if number % 2 == 0 else 1)
            new_line = line[:index] + '[' + str(left) + ',' + str(right) + ']' + line[index+2:]
            return new_line
    return None


def run():
    lines = [x.strip() for x in open('test2.txt', 'r').readlines()]
    line = None
    for input_line in lines:
        print(input_line)
        if line is None:
            line = input_line
        else:
            line = '[' + line + ',' + input_line + ']'
        line = reduce_number(line)
    line = reduce_number(line)
    number = make_number(line, 0)
    print(number)
