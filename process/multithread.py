#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, threading, random;

# def loop():
    # print 'thread %s is running...' % threading.current_thread().name;
    # n = 0;
    # while n < 5:
        # n += 1;
        # print 'thread %s >>> %s' % (threading.current_thread().name, n);
        # time.sleep(random.random());
    # print 'thread %s ended.' % threading.current_thread().name;

# print 'thread %s is running...' % threading.current_thread().name;
# l = list();
# for i in range(3):
    # t = threading.Thread(target = loop, name = 'LoopThread' + str(i));
    # t.start();
    # l.append(t);
# for i in range(3):
    # l[i].join();
# print 'thread %s ended.' % threading.current_thread().name;

##############################################################################
balance = 0;
lock = threading.Lock();

def change_it(n):
    global balance;
    balance += n;
    balance -= n;

def run_thread(n):
    for i in range(100000):
        lock.acquire();
        try:
            change_it(n);
        finally:
            lock.release();

t1 = threading.Thread(target = run_thread, args = (5,));
t2 = threading.Thread(target = run_thread, args = (8,));
t1.start();
t2.start();
t1.join();
t2.join();
print balance;

