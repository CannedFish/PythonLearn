#!/usr/bin/env python
# -*- coding: utf-8 -*-

L = ['a','b','c','d','e'];
r = [];
n = 3;
for i in range(n):
    r.append(L[i]);
print r;

print L[0:3];
print L[:3];
print L[1:3];
print L[2:5];
print L[-1:];

L = range(100);
print L[:10:2], L[::5];

print 'abcdefghijklmn'[::2];

