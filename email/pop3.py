#!/usr/bin/env python
# -*- coding: utf-8 -*-

import poplib;
import email;
from email.parser import Parser;
from email.header import decode_header;
from email.utils import parseaddr;

addrlist = [
    ('785358458@qq.com', 'pop3.qq.com'), 
    ('lianggy0719@126.com', 'pop3.126.com'), 
    ('guanyu@iscas.ac.cn', 'pop3.iscas.ac.cn')
];

def _show_list(l):
    num = 0;
    for item in l:
        print '%d. %s' % (num, item[0]);
        num += 1;

def decode_str(s):
  value, charset = decode_header(s)[0];
  if charset:
    value = value.decode(charset);
  return value;

def guess_charset(msg):
  charset = msg.get_charset();
  if charset is None:
    content_type = msg.get('Content-Type', '').lower();
    pos = content_type.find('charset=');
    if pos >= 0:
      charset = content_type[pos + 8:].strip().split(';')[0];
  return charset;

def print_info(msg, indent = 0):
  if indent == 0:
    for header in ['From', 'To', 'Subject']:
      value = msg.get(header, '');
      if value:
        if header == 'Subject':
          value = decode_str(value);
        else:
          hdr, addr = parseaddr(value);
          name = decode_str(hdr);
          value = u'%s <%s>' % (name, addr);
      print u'%s%s: %s' % ('  ' * indent, header, value);

  if (msg.is_multipart()):
    parts = msg.get_payload();
    for n, part in enumerate(parts):
      print '%spart %s' % (' ' * indent, n);
      print '%s----------------------------------' % ('  ' * indent);
      print_info(part, indent + 1);
  else:
    content_type = msg.get_content_type();
    if content_type == 'text/plain' or content_type == 'text/html':
      content = msg.get_payload(decode = True);
      charset = guess_charset(msg);
      if charset:
        # print 'Charset:', charset;
        content = content.decode(charset);
      print '%sText: %s' % ('  ' * indent, content + '...');
    else:
      print '%sAttachment: %s' % ('  ' * indent, content_type);

#email address
_show_list(addrlist);
choose = raw_input('Email: ');
email = addrlist[int(choose)][0];
#pop3 server
pop3_server = addrlist[int(choose)][1];
#password
password = raw_input('Password: ');

server = poplib.POP3(pop3_server);
server.set_debuglevel(1);
print server.getwelcome();
server.user(email);
server.pass_(password);
print 'Message: %s, Size: %s' % server.stat();

resp, mails, octets = server.list();
print mails;

idx = len(mails);
resp, lines, octets = server.retr(idx);
msg_content = '\r\n'.join(lines);
msg = Parser().parsestr(msg_content);
server.quit();
print_info(msg);

