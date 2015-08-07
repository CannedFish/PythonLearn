#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):

  def __init__(self, name = 'Unkonwn', score = 60):
    self.name = name;
    self.score = score;

  def print_score(self):
    print '%s: %s' % (self.name, self.score);

  def get_grade(self):
    if self.score >= 90:
      return 'A';
    if self.score >= 80:
      return 'B';
    if self.score >= 70:
      return 'C';
    if self.score >= 60:
      return 'D';
    return 'E';

a = Student('Bart', 59);
b = Student();
a.print_score();
b.print_score();

print a.get_grade(), b.get_grade();

