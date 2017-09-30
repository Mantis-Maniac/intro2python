# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

num = 1

while num < 2:
    
    url = 'http://duanziwang.com/2620.html'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)

    content = response.read().decode('utf-8')
    pattern = re.compile(u"[\u4e00-\u9fa5]+", re.DOTALL | re.I)
    #pattern = re.compile(r'\w+', re.DOTALL | re.I)
    items = re.findall(pattern, content)

    for item in items:
        print item
        

    num = num + 1
