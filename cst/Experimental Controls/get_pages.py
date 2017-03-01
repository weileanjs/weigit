import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import re
import lxml
import time
from multiprocessing import Pool
import time
from page_to_sql import page_to_sql3,saved_urls,err_urls, item_urls,s_urls,er_urls,del_url

cate = 'Experimental Controls'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Accept':'text/html, */*; q=0.01',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Accept-Encoding':'gzip, deflate, sdch',
'Connection':'keep-alive',
'Referer':'https://www.cellsignal.com/',
}


def price_page(p_url):
    req_p = requests.get(p_url,headers = headers)
    price_l = []
    soup_p = BeautifulSoup(req_p.text,'lxml')
    prices = soup_p.select('#purchase > tbody > tr > td:nth-of-type(3)')
    for price in  prices:
        if '现货查询' in price.text:
            price=str(price.text).replace('现货查询','').strip()
            price_l.append(price)
        else:
            price_l.append(str(price.text).strip())
    return  price_l

def to_size(size_n,size_q):
    size_dict = {}
    for n,q in zip(size_n,size_q):
        size_dict[n.text]=str(q.text).strip()
    return size_dict


def to_pid(ks,vs):
    pid_dict ={}
    for k,v in zip(ks,vs):
        pid_dict[k.text.strip()] = v.text.strip()
    return pid_dict

# price_page('http://www.cst-c.com.cn/products/8059.html')
def get_page(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text,'lxml')
    art_no_ = re.search(r'<h1 class="title" itemprop="name"> (.+?)</h1>',req.text).group(1)
    id = ''
    category = cate
    supplier = 'cst'
    art_no = art_no_.split('#')[1]
    name = art_no_.split('#')[0].split("&")[0]
    size_n =  soup.select('#purchase-list > tbody > tr > td.product-no')
    size_q =  soup.select('#purchase-list > tbody > tr > td.product-size')
    size = to_size(size_n,size_q)
    data_sheet = 'https://media.cellsignal.com/pdf/{}.pdf'.format(art_no)
    url = url
    storage = re.search('<b>Storage: </b>(.+?)</div>',req.text,re.S).group(1).strip()
    price = price_page('http://www.cst-c.com.cn/products/{}.html'.format(art_no))
    description = re.search('<p>(.+?)</p></br>',req.text).group(1)
    pid_k = soup.select('div > div > div > table > tbody > tr > td.product-attribute-value-productIncludes')
    pid_v = soup.select('div > div > div > table > tbody > tr > td.product-attribute-value-quantity')
    pid = to_pid(pid_k,pid_v)
    print('id:',id,
      'category:',category,
      'art_no:',art_no,
      'name:',name,
      'size:',size,
      'url:',url,
      'storage:',storage,
      'price:',price,
      'description:',description,
      'data_sheet:',data_sheet,
      'pid',pid)
    page_to_sql3(category,art_no,name,size,url,storage,price,description, data_sheet,pid)

left = list(set(item_urls())-set(s_urls()))
print(len(left))



# for u in  item_urls():
#     print(u)
#     try:
#         get_page(u)
#         saved_urls(u)
#         del_url(u)
#     except Exception as e:
#         print(e)
#         err_urls(u,e)


# get_page('https://www.cellsignal.com/products/buffers-dyes/immunohistochemistry-application-solutions-kit-rabbit/13079?N=102284+4294956287&fromPage=plp')





# print(req.text)

# print(search)
#purchase-list > tbody > tr > td.product-no

# saved = pd.DataFrame(list(db['saved_items'].find()))['saved'].tolist()
# err = pd.DataFrame(list(db['outlist'].find()))['outlist'].tolist()
