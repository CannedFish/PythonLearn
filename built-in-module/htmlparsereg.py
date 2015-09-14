#!/usr/bin/env python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser;
from htmlentitydefs import name2codepoint;

class MyHTMLParser(HTMLParser):

  def __init__(self):
    HTMLParser.__init__(self);
    self.count = 0;

  def handle_starttag(self, tag, attrs):
    print '%s<%s>, attrs: %s' % (self.count * '  ', tag, attrs);
    if tag != 'br':
      self.count += 1;

  def handle_endtag(self, tag):
    self.count -= 1;
    print '%s</%s>' % (self.count * '  ', tag);

  def handle_startendtag(self, tag, attrs):
    print '<%s/>' % tag;

  def handle_data(self, data):
    print '%sdata: %s' % (self.count * '  ', data);

  def handle_comment(self, data):
    print '<!-%s->' % data;

  def handle_entityref(self, name):
    print '&%s;' % name;

  def handle_charref(self, name):
    print '&#%s;' % name;

parser = MyHTMLParser();
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial..<br>End</p></body></html>');

