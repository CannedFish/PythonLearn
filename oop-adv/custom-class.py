#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Record(object):
  def __init__(self, info):
    self.__info = info;
  def __len__(self):
    return 99;
  def __str__(self):
    return 'Info of this record is %s' % self.__info;
  __repr__ = __str__;
  def __getattr__(self, attr):
    if attr == 'length':
      return 999;

r = Record('hahahahahahahahah');
print len(r);
print r, r.length;

class Chain(object):
  def __init__(self, path = ''):
    self.__path = path;
  def __getattr__(self, path):
    return Chain('%s/%s' % (self.__path, path));
  def __str__(self):
    return self.__path;
  def users(self, user):
    return Chain('%s/%s' % (self.__path, user));
  def __call__(self):
    return 'You call me';

print Chain('localhost:8888').status.user.timeline.list;
print Chain('localhost:8888').users('simon').repos;
chain = Chain();
print chain(), callable(chain);

class Fib(object):
  def __init__(self):
    self.__a = 0;
    self.__b = 1;
  def __iter__(self):
    return self;
  def next(self):
    self.__a, self.__b = self.__b, self.__a + self.__b;
    if self.__a > 100:
      raise StopIteration();
    return self.__a;
  def __getitem__(self, n):
    if isinstance(n, int):
      a, b = 1, 1;
      for x in range(n):
        a, b = b, a + b;
      return a;
    if isinstance(n, slice):
      start = n.start;
      stop = n.stop;
      a, b = 1, 1;
      L = [];
      for x in range(stop):
        if x >= start:
          L.append(a);
        a, b = b, a + b;
      return L;

fib = Fib();
for n in fib:
  print n;
print fib[5];
print fib[4:10];

# https://docs.python.org/2/reference/datamodel.html#special-method-names
