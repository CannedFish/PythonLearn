#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
    pass;

def set_age(self, age):
    self.__age = age;

def age(self):
    return self.__age;

s = Student();
from types import MethodType;
s.set_age = MethodType(set_age, s, Student);
s.set_age(23);

s.age = MethodType(age, s, Student);
print s.age();

def set_score(self, score):
    self.__score = score;

def score(self):
    return self.__score;

Student.set_score = MethodType(set_score, None, Student);
Student.score = MethodType(score, None, Student);

s2 = Student();
s2.set_score(19);
print s2.score();

class Person(object):
    __slots__ = ('name', 'age');

p = Person();
p.name = 'A';
p.age = 15;

class Man(Person):
    pass;

m = Man();
m.name = 'm';
m.age = 123;
m.sex = 'male';

