#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lazy_sum(*agrs):
  def sum():
    ax = 0;
    for n in agrs:
      ax += n;
    return ax;
  return sum;

fn = lazy_sum(1, 4, 5, 7, 8);
print fn();

print
def count():
  fs = [];
  for i in range(1, 4):
    fs.append((lambda j = i: j*j));
  return fs;
f1, f2, f3 = count();
print f1(), f2(), f3();
f1, f2, f3 = [(lambda j = i: j * j) for i in range(1, 4)];
print f1(), f2(), f3();

