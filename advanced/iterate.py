#!/usr/bin/env python
# -*- coding: utf-8 -*-

L = range(10, 100, 10);
for key in L:
  print key;
for i in range(len(L)):
  print L[i];

print
D = {'a': 1, 'b': 2, 'c': 3};
for key in D:
  print key, D[key];

print
from collections import Iterable
print 'abc', isinstance('abc', Iterable);
print '[1, 2, 3]', isinstance([1, 2, 3], Iterable);
print 123, isinstance(123, Iterable);

print
for idx, v in enumerate(['a', 'b', 'c']):
  print idx, v;

for x, y in [(0, 1), (1, 9), (4, 5)]:
  print x, y;
