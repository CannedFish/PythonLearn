#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email import encoders;
from email.header import Header;
from email.mime.text import MIMEText;
from email.mime.base import MIMEBase;
from email.mime.multipart import MIMEMultipart;
from email.utils import parseaddr, formataddr;
import smtplib, sys;

try:
    subject = sys.argv[1];
except:
    subject = 'A Fish to itself.';

def _format_addr(s):
    name, addr = parseaddr(s);
    return formataddr((Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr));

addrlist = [
    ('785358458@qq.com', 'smtp.qq.com'), 
    ('lianggy0719@126.com', 'smtp.126.com'), 
    ('guanyu@iscas.ac.cn', 'smtp.iscas.ac.cn'),
    ('wangbo@iscas.ac.cn', 'smtp.iscas.ac.cn')
];

def _show_list(l):
    num = 0;
    for item in l:
        print '%d. %s' % (num, item[0]);
        num += 1;

# from addr
_show_list(addrlist);
choose = raw_input('From: ');
from_addr = addrlist[int(choose)][0];
# smtp server
smtp_server = addrlist[int(choose)][1];
# password
password = raw_input('Password: ');
# to addr
_show_list(addrlist);
choose = raw_input('To: ');
to_addr = addrlist[int(choose)][0];

msg = MIMEMultipart();
msg['From'] = _format_addr('CannedFish <%s>' % from_addr);
msg['To'] = _format_addr('OtherFish <%s>' % to_addr);
msg['Subject'] = Header(subject, 'utf-8').encode();

msg.attach(MIMEText('<html><body><h1>Hello</h1><p>send by '
    + '<a href="http://www.python.org">Python</a>..</p>'
    + '<p><img src="cid:0"></p></body></html>', 'html', 'utf-8'));
with open('./0.jpg', 'rb') as f:
    mine = MIMEBase('image', 'jpg', filename = '0.jpg');
    mine.add_header('Content-Disposition', 'attachment', filename = '0.jpg');
    mine.add_header('Content-ID', '<0>');
    mine.add_header('X-Attachment-Id', '0');
    mine.set_payload(f.read());
    encoders.encode_base64(mine);
    msg.attach(mine);

server = smtplib.SMTP(smtp_server, 25);
server.set_debuglevel(1);
server.login(from_addr, password);
server.sendmail(from_addr, [to_addr], msg.as_string());
server.quit();

