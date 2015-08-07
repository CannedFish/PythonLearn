#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

print '10 / 3', 10 / 3;

import myModule.a;

myModule.a.test();

try:
    import cStringIO as StringIO;
except ImportError:
    print ImportError;
    import StringIO;

import myModule.b;

print myModule.b.greeting('ab'), myModule.b.greeting('abcd');

