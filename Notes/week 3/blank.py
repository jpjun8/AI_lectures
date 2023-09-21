import numpy as np

c = np.array(['a1b2', '1b2a', 'b2a1', '2a1b'])

print(np.char.capitalize(c))

print(np.char.center(c, width=9))
print(np.char.center(c, width=9, fillchar='*'))
print(np.char.center(c, width=2))

print(np.char.encode(c, encoding='UTF8'))

print(np.char.join('-', 'abc'))
print(np.char.join(['-', '.'], ['abc', 'def']))
