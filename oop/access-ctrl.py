#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person(object):

    def __init__(self, name, sex):
        self.__name = name;
        self.__sex = sex;

    def info(self):
        print '%s -> %s' % (self.__name, self.__sex);

    def setName(self, name):
        if not isinstance(name, str):
            print 'bad name!';
            return ;
        self.__name = name.title();

    def getName(self):
        return self.__name;

    def setSex(self, sex):
        if sex != 'male' and sex != 'famale':
            print 'bad sex';
            return ;
        self.__sex = sex;

    def getSex(self):
        return self.__sex;

tom = Person('Tom', 'male');
jerry = Person('Jerry', 'famale');

tom.info();
jerry.info();

print tom.getName(), tom.getSex();

tom.setName('xnekx');
tom.setSex('famale');
tom.info();

jerry.setName(23423);
jerry.setSex('man');
jerry.info();

jerry._Person__name = 'Jason';
jerry.info();

