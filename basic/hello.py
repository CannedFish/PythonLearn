#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'hello, world';

print 'This is a new sentance', 'OK';

# aba = raw_input('Please input sth: ');
# print 'Input is:', aba;

#indent

print '''line1
lien2
line3'''
print

print 3 > 2, 4 > 5;
print

print 3 > 2 and 4 > 5;
print 3 > 2 or 4 > 5;
print not 4 > 5;

print
print None == 0;

print
a = 'abd';
b = a;
print a, b;
a = 'xyz'
print a, b;

print
print u'中文';

print
print 'You are %s %d 0x%x' % ('some one', 123, 123);

print
teammates = ['aa', 'bb', 'cc'];
print 'teammates:', teammates, len(teammates), teammates[0], teammates[-1];
teammates.append('dd');
print 'teammates:', teammates;
teammates.insert(2, 'ff');
item = teammates.pop();
print teammates, item;
teammates[2] = 1234;
teammates.insert(1, True);
teammates.sort();
print teammates;

print
teammates = ('123', 'ddd', False);
print teammates;
ll = ['a', 'b'];
teammates = ('123', '456', ll);
print teammates;
teammates[2][0] = 'c';
teammates[2][1] = 'd';
print teammates;

print
for item in teammates:
    print item;

print
sum = 0
for i in range(101):
    sum += i;
print sum;

# while True:
    # num = int(raw_input('Please input a num:'));
    # if(num > 0):
        # print 'positive';
    # elif(num < 0):
        # print 'negative';
    # else:
        # print 'zero';

print
score = {'a': 99, 'b': 22, 'c': 43};
for key in score:
    print '%s: %d' % (key, score[key]);
print score.pop('a');

print
keys1 = set([1, 2, 4, 4, 3, 6, 9, 9]);
keys2 = set([1, 2, 3, 6, 10, 5]);
print keys1 | keys2;
print keys1 & keys2;

