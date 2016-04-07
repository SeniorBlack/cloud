#!/usr/bin/env python
# coding=utf8
# File: restful_client.py

import urllib2


def http_get():
    url = 'https://api.newrocktech.com/v1/devices?user_id=3839953797&access_token=NTU5OGNlYmMt.WZhOS00ZWI3LWIzMWQtOTQ5ZDg4MzBmYzg0'
#   url = 'https://www.baidu.com/'
    response = urllib2.urlopen(url)
    return response.read()

ret = http_get()
print ret
