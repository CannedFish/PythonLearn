#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re;
m = re.search('(?<=abc)def', 'abcdef');
print m.group(0);

