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

    scores = []
    for line in lines:
        is_corrupted = False
        queue = []
        for item in line:
            if item in chunk_open:
                queue.append(item)
            elif item in chunk_close:
                last_open = queue.pop()
                if item != chunk_open_close.get(last_open):
                    is_corrupted = True
                    break
            else:
                print("Invalid character!")
                is_corrupted = True
                break
        if is_corrupted is False and len(queue) > 0:
            # print(f"incomplete: {line}")
            sum = 0
            # print(queue)
            for missing_close in reversed(queue):
                # print(missing_close)
                if missing_close == '(':
                    sum = sum * 5 + 1
                elif missing_close == '[':
                    sum = sum * 5 + 2
                elif missing_close == '{':
                    sum = sum * 5 + 3
                elif missing_close == '<':
                    sum = sum * 5 + 4
            print(sum)
            scores.append(sum)

    scores.sort()
    print("Total:")
    print(scores[len(scores) // 2])
