#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
en = base64.b64encode('binary\x00string');
dn = base64.b64decode(en);
print '%s <==> %s' % (en, dn);

print base64.b64encode('i\xb7\x1d\xfb\xef\xff');
sen = base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff');
sdn = base64.urlsafe_b64decode(sen);
# print 'safe url: %s <===> %s' % (sen, sdn);

def safe_b64decode(b64str):
  pedding = 4 - len(b64str) % 4;
  b64str += '=' * pedding;
  return base64.b64decode(b64str);
print safe_b64decode('YWJjZA');

