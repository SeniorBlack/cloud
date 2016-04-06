# coding=utf8
from email.mime.text import MIMEText
msg = MIMEText('hello,send by Python...', 'plain', 'utf-8')

# 输入email地址和口令
from_addr = raw_input('From: ')
password = raw_input('Password: ')

# 输入SMTP服务器地址
# smtp_server = raw_input('SMTP server: ')
