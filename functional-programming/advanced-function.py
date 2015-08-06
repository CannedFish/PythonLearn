#!/usr/bin/env python
# -*- coding: utf-8 -*-

xx = abs;
print xx(-999), xx(999);

print
def abadd(x, y, f):
    return f(x) + f(y);
print abadd(-9, -11, abs);

# The advanced function means a function who has one or more parameters are a function.

print 
def f(x):
    return x * x;
print map(f, range(10));
print map(str, range(10));

print
def f(x, y):
    return x * 10 + y;
print reduce(f, range(10));

print;
def str2int(s):
    def fn(x, y):
        return x * 10 + y;
    D = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9};
    def char2num(s):
        return D[s];
    return reduce(fn, map(char2num, s));
print str2int('393483719238349');

print;
def str2int1(s):
    D = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9};
    def char2num(s):
        return D[s];
    return reduce(lambda x, y: x * 10 + y, map(char2num, s));
print str2int1('239481354819085390');

print;
def prod(l):
    def p(x, y):
        return x * y;
    return reduce(p, l);
print prod([1, 2, 3, 4, 5]);

print;
def firstUp(l):
    def u(s):
        return s.title();
    return map(u, l);
print firstUp(['adam', 'LISA', 'barT']);

print;
def is_odd(n):
    return n & 1 == 1;
print filter(is_odd, range(10));

print;
L = [34, 44, 2, 1, 55, 38];
print sorted(L);

def reversed_cmp(x, y):
    if x > y:
        return -1;
    if x < y:
        return 1;
    return 0;
print sorted(L, reversed_cmp);

