#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re;

rex = r'^(\d{3})\-(\d{3,8})$';
re_telephone = re.compile(rex);
print re_telephone.match('010-43493');
print re_telephone.match('010-43493s');
m = re_telephone.match('010-4349349');
print m.groups();

s = 'a,b;; c  d ,e';
print re.split(r'[\s\,\;]+', s);

rex1 = r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$';
m1 = re.match(rex1, '19:05:30');
print m1.groups();

re_email = re.compile(r'^([a-zA-Z][a-zA-Z0-9\.]*)\@([a-zA-Z0-9\.]+)');
print re_email.match('someone@gmail.com').groups();
print re_email.match('someone@126.com').groups();
print re_email.match('someone.bill.gates@gmail.com').groups();

re_email1 = re.compile(r'^\<([\w\s]+)\>\s+([a-zA-Z][a-zA-Z0-9\.]*)\@([a-zA-Z0-9\.]+)');
print re_email1.match('<tony parker> someone@gmail.com').groups();
print re_email1.match('<tony parker> someone@126.com').groups();
print re_email1.match('<tony parker> someone.bill.gates@gmail.com').groups();

