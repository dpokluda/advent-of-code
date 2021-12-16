# empty list
l = []
print(l)

#  initialized list
l = [0 for _ in range(0, 10)]
print(l)

# list
l = [x for x in range(0, 10)]
print(l)

# check existence
print(0 in l)

# comprehension
# newlist = [expression for item in iterable if condition == True]
print([x**2 for x in l if x % 2 == 0])

# sort
l.sort()
l.sort(reverse=True)
print(l)

# reverse
l.reverse()
print(l)

# slicing
print('first two:', l[:2])
print('all but last two:', l[:-2])
print('last two:', l[-2:])
print('all but first two:', l[2:])
print('every second:', l[::2])
print('reversed:', l[::-1])

# cloning list
c = l[:]
print(c)
