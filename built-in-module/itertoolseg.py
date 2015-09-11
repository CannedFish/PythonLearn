#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

cs = itertools.repeat('AB', 10);
for c in cs:
  print c;

natuals = itertools.count(1);
ns = itertools.takewhile(lambda x: x <= 10, natuals);
for n in ns:
  print n;

for c in itertools.chain('ABC', 'XYZ'):
  print c;

for key, group in itertools.groupby('AaaBbBCcAaA', lambda c: c.upper()):
  print key, list(group);

for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
  print x;

r = itertools.imap(lambda x: x * x, itertools.count(1));
for n in itertools.takewhile(lambda x: x <= 100, r):
  print n;

