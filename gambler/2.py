import urllib.request
import requests
n1 = 'http://www.dianping.com/search/category/3/10/p1'
def open_url(url):

    # proxy = 'http://122.72.2.180:8080'
    # opener = urllib2.build_opener(urllib2.ProxyHandler({'http':proxy}), urllib2.HTTPHandler(debuglevel=1))
    # urllib2.install_opener(opener)
    i_headers = {'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
                 'User-Agent' :  'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US)'
                                  'AppleWebKit/534.16 (KHTML, like Gecko)'
                                  'Chrome/10.0.648.151 Safari/534.16'}
    req = requests.get(url,)

    # response=urllib.request.urlopen(req)
    # html = response.read().decode('utf-8',errors='replace')
    print(req.text)
a11=open_url(n1)
