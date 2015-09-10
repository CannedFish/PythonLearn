#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    with open('../README.md1', 'r') as f1:
        print f1.read();
except IOError, err:
    print 'IOError:', err;

f = open('../basic/hello.py', 'r');
i = 1;
for line in f.readlines():
    print "%3d  %s" % (i, line.strip());
    i += 1;
f.close();

with open('../README.md', 'a') as ff:
    ff.write('This is writen by code\n');

with open('../README.md', 'r') as ff:
    print ff.read();

