#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct, sys

filename = sys.argv[1];

try:
  pic = open(filename, 'rb');
  content = pic.read(30);
  info = struct.unpack('<ccIIIIIIHH', content);
  if info[0] == 'B' and info[1] == 'M':
    print 'Size: %dx%d, Color: %d.' % (info[6], info[7], info[-1]);
  else:
    print 'This is not a bmp picture.';
except IOError, e:
  print 'Error:', e;
except struct.error, e:
  print 'Error:', e;
finally:
  pic.close();

