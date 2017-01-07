from bs4 import BeautifulSoup
import requests
import time
import pymongo
client = pymongo.MongoClient('localhost',27017)
duanzhu = client['duanzhu']
bnb_info = duanzhu['sheet_tab']


def get_single_datas(link):
    wb_data = requests.get(link)
    soup = BeautifulSoup(wb_data.text,'lxml')
    # 因为是单页面，使用 select 方法获得的元素又是一个列表，那么列表中的第一个元素且也是唯一一个元素即是我们要找的信息 用 “[0]” 索引将其取出
    # 后在对其使用处理的方法，因为 beautifulsoup 的些筛选方法并不能针对列表类型的元素使用 ;)

    title = soup.select('div.pho_info > h4')[0].text
    address = soup.select('div.pho_info > p')[0].get('title') # 和 get('href') 同理，他们都是标签的一个属性而已，我们只需要的到这个属性的内容即可
    price = soup.select('div.day_l > span')[0].text
    pic = soup.select('#curBigImage')[0].get('src')   # “#” 代表 id 这个找元素其实就是找他在页面的唯一
    host_name = soup.select('a.lorder_name')[0].text
    data = {
        'title':title,
        'address':address,
        'price':price,
        'pic':pic,
        'host_name':host_name,
    }
    bnb_info.insert_one(data)

# -------------------补充------------------
# 如何批量获取链接

 # <- 每个详情页的链接都存在这里，解析详情的时候就遍历这个列表然后访问就好啦~

def get_page_link(page_number):
    page_link = []
    for each_number in range(1,page_number): # 每页24个链接,这里输入的是页码
        time.sleep(2)
        full_url = 'http://bj.xiaozhu.com/chaoyang-duanzufang-p{}-8/'.format(each_number)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        for link in soup.select('a.resule_img_a'): # 找到这个 class 样为resule_img_a 的 a 标签即可
             page_link.append(link.get('href'))
    return page_link


'''
all_links = get_page_link(2)[0:20]
for i in all_links:
    get_single_datas(i)
'''

# 从数据库中进行筛选
for i in bnb_info.find():
    if int(i['price']) >= 500:
        print(i['title'],i['price'])




