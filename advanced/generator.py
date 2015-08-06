#!/usr/bin/env python
# -*- coding: utf-8 -*-

g = (x * x for x in range(10));

for i in range(10):
  print g.next();

print
g1 = (x * x for x in range(10));
for n in g1:
  print n;

def fib(max):
  n, a, b = 0, 0, 1;
  while n < max:
    yield b;
    a, b = b, a + b;
    n = n + 1;
for n in fib(6):
  print n;

