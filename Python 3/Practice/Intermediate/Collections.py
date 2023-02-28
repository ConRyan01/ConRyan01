#collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

a = "aaabbbbcccdddeeeeee"
my_counter = Counter(a)
print(my_counter) #try my_counter.keys() and my_counter.items() as well
print(my_counter.most_common(1)) #arg is amount of most common keys and items
print(list(my_counter.elements()))

from collections import namedtuple
point = namedtuple('point', 'x,y') #creates class called point with args x and y
pt = point(1,-4)
print(pt)

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 2
print(ordered_dict)

from collections import defaultdict #created default values for undefined elements
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)

print(d)