#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):

  def __init__(self, name):
    self.__name = name;

  @property
  def score(self):
    return self.__score;

  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer.');
    if value < 0 or value > 100:
      raise ValueError('score must between 0 ~ 100.');
    self.__score = value;

  @property
  def name(self):
    return self.__name;

s = Student('Simon');
s.score = 90;
print s.name, s.score;

