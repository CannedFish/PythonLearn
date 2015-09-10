#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os;

print os.name;
print os.uname();
print os.environ;

print os.getenv('PATH');
print os.getenv('HOME');

print os.path.abspath('.');

# os.mkdir('testDir');
# os.rename('testDir', 'abc');
os.rmdir('abc');

