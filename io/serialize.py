#!/usr/bin/env python
# -*- coding; utf-8 -*-

try:
  import cPickle as pickle;
except ImportError:
  print 'no cPickle';
  import pickle;

d = dict(name = 'Bob', age = 20, score = 88);
print 'Origin:', d;

d['empty'] = 'xxxx';
print 'Modify:', d;
f = open('dump', 'wb');
pickle.dump(d, f);
f.close();

f = open('dump', 'rb');
d = pickle.load(f);
f.close();
print 'Load:', d;

import json;

d = dict(name = 'Alice', age = 21, score = 99);
print 'Origin:', d;

d['sex'] = 'famale';
print 'Modify:', d;
f = open('dump', 'wb');
json.dump(d, f);
f.close();

f = open('dump', 'rb');
d = json.load(f);
f.close();
print 'Load:', d;

class Student(object):
  def __init__(self, name, age, score):
    self.name = name;
    self.age = age;
    self.score = score;

s = Student('Bob', 20, 88);

# def stu2dict(std):
  # return {
      # 'name': std.name,
      # 'age': std.age,
      # 'score': std.score
  # };
# print json.dumps(s, default = stu2dict);
print json.dumps(s, default = lambda obj: obj.__dict__);

def dict2std(d):
  return Student(d['name'], d['age'], d['score']);
s = '{"age": 20, "score": 88, "name": "Bob"}';
print json.loads(s, object_hook = dict2std);

