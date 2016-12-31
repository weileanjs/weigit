import re
import time
import numpy as np
import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Accept':'text/html;q=0.9,*/*;q=0.8', 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Connection':'close', 'Referer':'http://bzclk.baidu.com/' }
url2 = 'https://www.we.com/loan#page-2'
url='http://www.dianping.com/search/category/3/10/p2'
req=urllib.request.Request(url=url,headers = headers)
resq=urllib.request.urlopen(req,timeout=2)
html=resq.read().decode('utf-8',errors='replace')
amount=re.findall(r'data-key="(.*?)"',html)
#amount=re.findall(r'"amount":(.*?),',html)
print(amount[0])

#r'(data-key="(.*?)" (.*?);" alt="">(.*?))
