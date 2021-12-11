def run():
    file = open('input.txt', 'r')
    data = file.readlines()
    previous = None
    count = 0
    for value in data:
        int_value = int(value)
        if int_value > 0:
            # print(int_value)
            if previous is not None and previous < int_value:
                count += 1
            previous = int_value
    print(count)
