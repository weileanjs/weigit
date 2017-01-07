import requests
import json
url = 'http://wap.dianping.com/shoplist/3/r/0/c/10/s/s_3/p1'
params = {'start':50,'regionid':0,'categoryid':10,'ortid':3,'locatecityid':3,'cityid':3,'allback':'jsonp1481703121743'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
           'Accept':'*/*',
           #'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Language':'zh-CN,zh;q=0.8',
           'Accept-Encoding':'gzip, deflate, sdch',
           'Connection':'keep-alive',
           'Host':'mapi.dianping.com',
           'Cookie':'_hc.v=1175b9f3-28fd-2977-0f07-8901226a80ed.1481553540; dper=1d6be6dac42ee65736faaa01e27bcfe03c4485eeadaf3aded0ed9b0a5f6c1a63; ua=weileanjs; s_ViewType=10; aburl=1; cy=3; cye=hangzhou; PHOENIX_ID=0a060c39-158fc091992-ad8309; ll=7fd06e815b796be3df069dec7836c3df; pvhistory="6L+U5ZuePjo8L3N0YXRpY3Rlc3QvbG9nZXZlbnQ/bmFtZT1XaGVyZUFtSUZhaWwmaW5mbz1odG1sLSU1QiU3QiUyMmNvZGUlMjIlM0ExJTJDJTIybWVzc2FnZSUyMiUzQSUyMk9ubHklMjBzZWN1cmUlMjBvcmlnaW5zJTIwYXJlJTIwYWxsb3dlZCUyMChzZWUlM0ElMjBodHRwcyUzQSUyRiUyRmdvby5nbCUyRlkwWmtOVikuJTIyJTdEJTVEJmNhbGxiYWNrPVdoZXJlQW1JMTE0ODE2OTczODIzNzA+OjwxNDgxNjk3Mzg0NDEzXV9b"; m_flash2=1; issqt=false; sqttype=0; cityid=3; msource=default; default_ab=shopList%3AA%3A1',
           'Referer':'http://wap.dianping.com/shoplist/3/r/0/c/10/s/s_3/p1'}



res = requests.get(url)
#data = res.json()
print(res.text)

