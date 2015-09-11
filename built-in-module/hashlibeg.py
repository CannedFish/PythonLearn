#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

ori = 'how to use md5 in python hashlib?';
md5 = hashlib.md5();
md5.update(ori);
print 'md5: (%s) ==> (%s).' % (ori, md5.hexdigest());

sha1 = hashlib.sha1();
sha1.update(ori);
print 'sha1: (%s) ==> (%s).' % (ori, sha1.hexdigest());

def calc_md5(passwd):
  md5 = hashlib.md5();
  md5.update(passwd);
  return md5.hexdigest();

db = {
    'michael': calc_md5('123456'),
    'bob': calc_md5('123'),
    'alice': calc_md5('456')
};

while True:
  user = raw_input('Username: ');
  passwd = raw_input('Password: ');
  try:
    if db[user] == calc_md5(passwd):
      print 'Login successfully!';
    else:
      print 'Username or password is wrong!';
  except KeyError, e:
    print 'Username or password is wrong!';

