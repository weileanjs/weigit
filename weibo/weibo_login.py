#导入requests库(请求和页面抓取)
import requests
#导入正则库（从页面代码中提取信息）
import re
#导入pandas库(用于创建数据表和导出csv)
import pandas as pd
payload = {'username': 'weileanjs@gamil.com','password': 'wchswb271828'}
url1='https://passport.weibo.cn/signin/login'
url2='http://weibo.com/askcliff/home'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Accept':'*/*',
'Accept-Charset':'zh-CN,zh;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Connection':'keep-alive',
'Referer':'http://weibo.com/weileanjs/home?wvr=5'
}

cookie={'SINAGLOBAL=6603853679511.278.1479369824909; UOR=www.tripadvisor.cn,widget.weibo.com,bbs.hcharts.cn; TC-Ugrow-G0=0149286e34b004ccf8a0b99657f15013; login_sid_t=f608eaff4fc57e2f32692507c2b67a0c; TC-V5-G0=784f6a787212ec9cddcc6f4608a78097; WBStorage=194a5e7d191964cc|undefined; _s_tentry=-; TC-Page-G0=0dba63c42a7d74c1129019fa3e7e6e7c; Apache=9591898830759.697.1483965841126; ULV=1483965841132:2:1:1:9591898830759.697.1483965841126:1479369824934; SCF=AjjSPX83-I2obpZCJfXXJ4w_QPmNCNREeKv4SpZH2lgrKlpQSPZVy_r3ylK2ZQBfWJKkqNFvE7J7Jyym2_ZwMPU.; SUB=_2A251d_ZeDeRxGedL4lsW9ivEyTiIHXVWBWCWrDV8PUNbmtAKLU3hkW8mAzCvMOasZbcWc2n5rKS1any0zA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWk2dTxM2c.ux03szW1dv3J5JpX5KzhUgL.Fo2f1K.NSo-ReoB2dJLoI7_N9gLoIsHVIs8V97tt; SUHB=079i2FJCg-vfwP; ALF=1515501966; SSOLoginState=1483965966; wvr=6'}

#设置一个会话对象
s = requests.Session()
#以post形式提交登陆用户名和密码
req=s.post(url=url1, data=payload, headers=headers)
req.encoding = 'SO-8859-1'
req.encoding = 'gb2312'
# r=requests.get(url=url2, cookies=cookie, headers=headers)
# #获取页面的内容信息
# html=r.content
# #对页面内容进行编码
# html=str(html, encoding = "UTF-8")
print(req.text)
