import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import lxml
import time
import os
from multiprocessing import Pool
# proxies = {"http": "http://111.124.205.31:80","https": "https://111.124.205.31:80"}



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Accept':'text/html, */*; q=0.01',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Accept-Encoding':'gzip, deflate, sdch',
'Connection':'keep-alive',
'Referer':'http://www.abcam.com/products?selected.productType=Primary+antibodies&pageNumber=2',
}
base_url = 'http://www.abcam.com/products?selected.productType=Primary+antibodies&pageNumber={}'
def all_pages():
    all_pages_url = [base_url.format(i) for i in [7588,7683]]
    data_1 = pd.DataFrame({"page_url":all_pages_url})
    data_1.to_csv(r'item_url\saved_urls\all.csv')
all_urls = set(pd.read_csv(r'item_url\all_pages_url.csv')['page_url'].tolist())

#7588,7683
def sved_url(path):
    list = []
    for file in os.listdir(path):
        list.append(file.split('.')[0])
    list.remove('all_pages_url')
    return  [base_url.format(i) for i in list ]
saved_urls = sved_url(r'item_url')

# print(len(set(all_urls)),len(set(saved_urls)),(len(set(all_urls))-len(set(saved_urls))))
# left_urls =set(all_urls)-set(saved_urls)
# print('left:',len(set(all_urls))-len(set(saved_urls)))



def get_items(url):
    print(url)
    page_num = re.search('pageNumber=(\d+)',url).group(1)
    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.text,'lxml')
    items = soup.select('div.search_results > div > div.pws_left_panel > div > h3 > a')
    title = []
    item_url = []
    for i in items:
        title.append(i.text)
        item_url.append(i.get('href'))
    data = pd.DataFrame({'title':title,'url_s':item_url})
    data.to_csv(r'item_url\saved_urls\{}.csv'.format(page_num))
    time.sleep(2)
    print(page_num+'is ok')




def combine_(path):
    title_l = []
    url_l = []
    error_l = []
    for file in os.listdir(path):
        print(file)
        file_path = os.path.join(path,file)
        try:
            c_path = pd.read_csv(file_path)
        except UnicodeDecodeError:
            print(file,'~~~~~~~~~~~~~~~~~')
            error_l.append(file)


        title_l.extend(c_path['title'].tolist())
        url_l.extend(c_path['url_s'].tolist())

    print(url_l)
    print(title_l)
    print('_____________________________________')
    print(error_l)
    u_data = pd.DataFrame({'item_url':url_l,'item_title':title_l})
    u_data.to_csv('err.csv')
    # print(url_l)
    # print(len(title_l),len(url_l))



combine_(r'C:\Users\W.C.H\wchgit\test2_16\item_url\saved_urls')



# if __name__ == '__main__':
#     pool = Pool(processes=4)
#     pool.map(get_items,left_urls)
#     pool.close()
#     pool.join()


# get_items( 'http://www.abcam.com/products?selected.productType=Primary+antibodies&pageNumber=3')
