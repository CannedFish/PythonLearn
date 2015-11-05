#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('src.txt', 'w') as f:
    f.write('How many seas must a white dove sail\nBefore she sleeps in the sand');

with open('src.txt', 'r') as f, open('dst.txt', 'w') as f2:
    f2.write(f.read());

with open('dst.txt', 'r+') as f2:
    content = f2.read();
    f2.seek(0, 0);
    f2.write('How many roads must a man walk down\nBefore they call him a man\n' + content);

with open('src.txt', 'r') as f, open('dst.txt', 'r') as f2:
    print 'src.txt:\n%s' % f.read();
    print 'dst.txt:\n%s' % f2.read();

