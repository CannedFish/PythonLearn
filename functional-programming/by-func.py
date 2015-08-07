#!/usr/bin/env python
# -*- coding: utf-8 -*-

def int2(x, base = 2):
  return int(x, base);

print int2('10101010101110'), int2('101010100000000');

import functools

intb = functools.partial(int, base = 2);
print intb('1111'), int2('1111');

max2 = functools.partial(max, 10);
print max2(2, 4, 6), max2(11, 6);

