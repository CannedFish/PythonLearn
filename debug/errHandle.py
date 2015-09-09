#!/usr/bin/env python
# -*- coding: utf-8 -*-

def foo():
    r = list();
    if r == (-1):
        return (-1);
    return r;

print foo();

try:
    print 'try..';
    r = 10 / int('a');
    print 'result:', r;
except ZeroDivisionError, e:
    print 'except:', e;
except ValueError, e:
    print 'ValueError:', e;
finally:
    print 'finally..';
print 'END';

import logging;

def fn(s):
    return 10 / int(s);

def sn(s):
    return fn(s) * 2;

def main():
    try:
        sn('0');
    except StandardError, e:
        # print 'Error:', e;
        logging.exception(e);
    finally:
        print 'finally..';

main();

class FooError(StandardError):
    pass;

def fn1(s):
    n = int(s);
    if n == 0:
        raise FooError('invalid value: %s' % s);
    return 10 / n;

fn1('0');

