#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_func(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type');
    if x >= 0:
        return x;
    else:
        return -x;

print my_func(20);
print my_func(-1);
# my_func('ADe');

print
def nop():
    pass;

def echo(s):
    print nop(), s;

echo('hello world');

print
import math;

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle);
    ny = y - step * math.sin(angle);
    return nx, ny;
x, y = move(100, 100, 60, math.pi / 6);
print x, y;

print
def power(x, n = 2):
    s = 1;
    while n > 0:
        n -= 1;
        s *= x;
    return s;
print power(5);
print power(5, 3);
# the default parameter must be immutable.

print
def calc(*number):
    sum = 0;
    for n in number:
        sum += n * n;
    return sum;
nums = [1, 2, 3];
print calc(1, 2), calc(), calc(*nums);

print
def person(name, age, **op):
    print 'name: %s, age: %d, op:' % (name, age), op;
person('Michael', 30);
person('Bob', 27, city = 'Beijing');
# func(*args, **kv)

print
def fact(n):
    return fact_iter(n, 1);
def fact_iter(n, product):
    if(n == 1):
        return product;
    return fact_iter(n - 1, n * product);
print fact(5), fact(10);

