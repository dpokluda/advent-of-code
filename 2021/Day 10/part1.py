chunks = [['(', ')'], ['[', ']'], ['{', '}'], ['<', '>']]


def run():
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]
    chunk_open = []
    chunk_close = []
    chunk_open_close = {}
    for chunk in chunks:
        chunk_open.append(chunk[0])
        chunk_close.append(chunk[1])
        chunk_open_close[chunk[0]] = chunk[1]

    invalid_characters = []
    for line in lines:
        is_corrupted = False
        queue = []
        for item in line:
            if item in chunk_open:
                queue.append(item)
            elif item in chunk_close:
                last_open = queue.pop()
                if item != chunk_open_close.get(last_open):
                    invalid_characters.append(item)
                    is_corrupted = True
                    break
            else:
                print("Invalid character!")
                is_corrupted = True
                break
        if is_corrupted:
            print(line)
    sum = 0
    for invalid_character in invalid_characters:
        if invalid_character == ')':
            sum += 3
        elif invalid_character == ']':
            sum += 57
        elif invalid_character == '}':
            sum += 1197
        elif invalid_character == '>':
            sum += 25137
        else:
            print(":-(")

    print("Sum:")
    print(sum)
