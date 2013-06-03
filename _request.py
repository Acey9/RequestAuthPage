#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# -----------------------------------------------------
#  FileName:    _request.py
#  Author  :    acey
#  Project :    
#  Date    :    2013-06-03
#  Descrip :    
# -----------------------------------------------------

import urllib
import urllib2
import cookielib

login_url = "http://10.255.250.81/user/login"

class RequestAuthPage(object):

    '''request authentication page'''

    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'}
    cookiejar = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cookiejar)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    def __init__(self, user, passwd, login_type='local'):
        self.user = user
        self.passwd = passwd
        self.login_type = login_type
    
    def login(self):
        user_data = {
            "user[account]":self.user,
            "user[password]":self.passwd,
            "login_type":self.login_type,
        }

        url_user_data = urllib.urlencode(user_data)
        req =  urllib2.Request(url=login_url, data=url_user_data, headers=self.headers)
        fd = urllib2.urlopen(req)
        content = fd.read()
        fd.close()

    def request(self, url):
        req =  urllib2.Request(url=url, headers=self.headers)
        fd = urllib2.urlopen(req)
        content = fd.read()
        http_code = fd.code
        fd.close()
        return http_code, content

if __name__ == '__main__':
    url = "http://10.255.250.81/assetReport/report"
    sc = RequestAuthPage('user', 'password')
    #login
    sc.login()

    #request
    code, content = sc.request(url)
    print content
