#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct

p = struct.pack('>I', 10240099);
print struct.unpack('>I', p);

pic = open('./test.bmp', 'rb');
content = pic.read(30);
print struct.unpack('<ccIIIIIIHH', content);

