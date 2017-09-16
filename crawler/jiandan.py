# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib
import urllib2
import re

#page = 1
num = 1
i = 0
#fo = open("foo.txt", "wb")
while num < 2000:
    url = 'http://jandan.net/duan/page-' + str(num)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        #print response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
    content = response.read().decode('utf-8')
    #print content
    pattern = re.compile('</span><p>.*</p>', re.I)
    items = re.findall(pattern,content)
    for item in items:
        #fo.write( str(i) + ": " + item[10:-4] + '\n')
        print str(i) + ": " + item[10:-4] + '\n'
        i = i + 1

    num = num + 1
