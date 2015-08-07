#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

def log(arg):
# or use callable to judge whether arg is a function or not
  if isinstance(arg, str):
    def decorator(func):
      @functools.wraps(func)
      def wrapper(*args, **kv):
        print '%s %s():' % (arg, func.__name__);
        return func(*args, **kv);
      return wrapper;
    return decorator;
  else:
    @functools.wraps(arg)
    def wrapper(*args, **kv):
      print 'call %s():' % (arg.__name__);
      return arg(*args, **kv);
    return wrapper;

@log
def now():
  print '2013-12-25';

now();
print now.__name__;

@log('execute')
def now2():
  print '2015-8-7';

now2();
print now2.__name__;

