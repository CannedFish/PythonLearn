#!/usr/bin/env python
# -*- coding: utf-8 -*-

print range(1, 11);
print [x * x for x in range(1, 11)];
print [m + n for m in 'ABC' for n in 'XYZ'];

import os;
print [d for d in os.listdir('.')];

D = {'a': 1, 'b': 2, 'c': 3};
for k, v in D.iteritems():
  print k, '=', v;

L = ['HDND', 'NDKEI', 23, 'DNKD', 123214];
print [s.lower() if isinstance(s, str) else s for s in L];

