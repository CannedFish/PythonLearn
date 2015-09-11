#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple;
Point = namedtuple('Point', ['x', 'y']);
p = Point(1, 2);
print p.x, p.y;

from collections import deque
q = deque(['a', 'b', 'c']);
q.append('x');
q.appendleft('y');
print q;

from collections import defaultdict
dd = defaultdict(lambda: 'N/A');
dd['key1'] = 'abc';
print dd['key1'], dd['key2'];

from collections import OrderedDict
d = dict([('c', 1), ('b', 2), ('a', 3)]);
print d;
od = OrderedDict([('c', 1), ('b', 2), ('a', 3)]);
print od;
print od.popitem(last = False);

from collections import Counter
c = Counter();
for ch in 'programming':
    c[ch] += 1;
print c;

