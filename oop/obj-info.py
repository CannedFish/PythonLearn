#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
  def run(self):
    print 'running..';

animal = Animal();
print type(animal);

print type(abs);
print type(123);

import types

print type('123') == types.StringType;
print type(123) == types.IntType;

print dir(animal);

print hasattr(animal, 'name');
setattr(animal, 'name', 'dog');
print hasattr(animal, 'name'), getattr(animal, 'name');
print getattr(animal, 'sex', 404);

