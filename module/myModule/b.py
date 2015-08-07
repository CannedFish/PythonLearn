#!/usr/bin/env python
# -*- coding: utf-8 -*-

'my second module'

__author__ = 'CannedFish';

def _prinvate_1(name):
  return 'Hello, %s' % name;

def _prinvate_2(name):
  return 'Hi, %s' % name;

def greeting(name):
  if len(name) > 3:
    return _prinvate_1(name);
  else:
    return _prinvate_2(name);

