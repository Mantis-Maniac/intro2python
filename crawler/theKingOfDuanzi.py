import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

num = 1
while num < 2:
    url = 'http://duanziwang.com/2757.html' 
    user_agent = 'Mozilla/4.0 (compatible; MSTE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    #print content
    
    pattern = re.compile('script>.</div>.<p>.*<h2', re.DOTALL | re.I) 
    items = re.findall(pattern, content)
    #items = re.search(r'<p>.*</p>', content, re.DOTALL|re.M|re.I)
    #print items.group()
    for item in items:
        print item
        #print item[10: -3]

    num = num + 1




