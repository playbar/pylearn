# itertools_cycle.py

from itertools import *

for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)


for i in repeat('over-and-over', 5):
    print(i)

for i, s in zip(count(), repeat('over-and-over', 5)):
    print(i, s)


for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
    print('{:d} * {:d} = {:d}'.format(*i))


