from collections import defaultdict

# empty
d = {}
print(d)

# initialized
d = {f'{x}': 0 for x in range(0, 10)}
print(d)

# check
print('a' in d)
d['a'] = 1
print('a' in d)
print(d)

# enumerate
d = {'a': 10, 'b': 20, 'c': 30}
for key in d:
    print(key)
for pair in d.items():
    print(pair)
for _, key in enumerate(d):
    print(key)

# clone
c = d.copy()
print(c)

# defaultdict
dd = defaultdict(int)
dd['a'] += 1
print(dict(dd))
