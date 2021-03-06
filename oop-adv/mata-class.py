#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Hello(object):
  def hello(self, name = 'world'):
    print('Hello, %s.' % name);

h = Hello();
h.hello();

print type(Hello);
print type(h);

def fn(self, name = 'world'):
  print 'Hello2, %s' % name;
Hello2 = type('Hello2', (object, ), dict(hello = fn));
h2 = Hello2();
h2.hello();

class ListMetaclass(type):
  def __new__(cls, name, bases, attrs):
    attrs['add'] = lambda self, value: self.append(value);
    return type.__new__(cls, name, bases, attrs);

class MyList(list):
  __metaclass__ = ListMetaclass;

L = MyList();
L.add(1);
print L;

print 

class Field(object):
  def __init__(self, name, column_type):
    self.name = name;
    self.column_type = column_type;
  def __str__(self):
    return '<%s:%s>' % (self.__class__.__name__, self.name);

class StringField(Field):
  def __init__(self, name):
    super(StringField, self).__init__(name, 'varchar(100)');

class IntergerField(Field):
  def __init__(self, name):
    super(IntergerField, self).__init__(name, 'bigint');

class ModelMetaclass(type):
  def __new__(cls, name, bases, attrs):
    if name == 'Model':
      return type.__new__(cls, name, bases, attrs);
    mappings = dict();
    for k, v in attrs.iteritems():
      if isinstance(v, Field):
        print 'Found mapping: %s ==> %s' % (k, v);
        mappings[k] = v;
    for k in mappings.iterkeys():
      attrs.pop(k);
    attrs['__table__'] = name;
    attrs['__mappings__'] = mappings;
    return type.__new__(cls, name, bases, attrs);

class Model(dict):
  __metaclass__ = ModelMetaclass;

  def __init__(self, **kv):
    super(Model, self).__init__(**kv);

  def __getattr__(self, key):
    try:
      return self[key];
    except KeyError:
      raise AttributeError(r"'Model' object has no attribute '%s'" % key);

  def __setattr__(self, key, value):
    self[key] = value;

  def save(self):
    fields = [];
    params = [];
    args = [];
    for k, v in self.__mappings__.iteritems():
      fields.append(v.name);
      params.append('?');
      args.append(getattr(self, k, None));
    sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params));
    print 'SQL: %s' % sql;
    print 'ARGS: %s' % str(args);

class User(Model):
  id = IntergerField('id');
  name = StringField('username');
  email = StringField('email');
  password = StringField('password');

u = User(id = 12345, name = 'Simon', email = 'aaa@qqq.com', password = 'passwd');
u.save();

