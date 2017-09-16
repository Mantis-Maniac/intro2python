# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

num = 1
#url = "https://www.qiushibaike.com/hot/page/1"
while num < 20:
    #url = 'http://jandan.net/duan/page-' + str(num)
    url = 'http://jandan.net/duan/page-' + str(num)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)

    content = response.read().decode('utf-8')
    pattern = re.compile('</span><p>.*</p>',re.I)
    items = re.findall(pattern, content)

    for item in items:
        print item
        print item[10: -3]

    num = num + 1
