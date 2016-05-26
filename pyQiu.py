# -*- coding: utf-8 -*-
import urllib
import cookielib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
page = 1
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36'
headers = { 'User-Agent' : user_agent }

for page in range(1,int(sys.argv[1])):
    try:
        cookie = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        url = 'http://www.qiushibaike.com/text/page/'+"%d"%page+"?s=4835048"
        request = urllib2.Request(url,headers = headers)
        response = opener.open(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('<div class="content">(.*?)<.*?></div>.*?<div class="stats">',re.S)
        items = re.findall(pattern,content)
        for item in items:
            print item
        page+=1
        print url
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
            if hasattr(e,"reason"):
                print e.reason

