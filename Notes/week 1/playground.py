from itertools import count
from itertools import cycle
from itertools import repeat
from itertools import islice
from itertools import chain
from itertools import combinations
from itertools import permutations
from itertools import product
from itertools import compress
from itertools import dropwhile
from itertools import takewhile

import heapq

import numpy as np

from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple
from collections import OrderedDict
from collections import ChainMap

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print(p._fields)
p = p._replace(x=10)
print(p)