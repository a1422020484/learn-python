from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


#from_addr = input('From: ')
#password = input('Password: ')
#to_addr = input('To: ')
#smtp_server = input('SMTP server: ')

from_addr = '1422020484@qq.com'
#password = 'wxyz4214769'
# 这个授权码可以有多个
POP3SMTP = 'wembryqmbrfnjabc'
IMAPSMTP = 'ecjhqriavvchijji'
to_addr = '2737198959@qq.com'
smtp_server = 'smtp.qq.com'


msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
#server.set_debuglevel(1)
server.login(from_addr, POP3SMTP)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
