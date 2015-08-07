#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
  pass;

class Manmal(Animal):
  pass;

class Bird(Animal):
  pass;

class Runnable(object):
  def run(self):
    print 'Running..';

class Flyable(object):
  def fly(self):
    print 'Flying..';

class CarnivorousMixin(object):
  def eat(self):
    print 'Eating meat..';

class HerbivoresMixin(object):
  def eat(self):
    print 'Eating plant..';

class Dog(Manmal, Runnable, CarnivorousMixin):
  pass;

class Bat(Manmal, Flyable, CarnivorousMixin):
  pass;

class Parrot(Bird, Flyable, HerbivoresMixin):
  pass;

class Ostrich(Bird, Runnable, HerbivoresMixin):
  pass;

d = Dog();
d.run();
d.eat();

p = Parrot();
p.fly();
p.eat();

