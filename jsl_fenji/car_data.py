from bs4 import BeautifulSoup
import requests
import time
import urllib
for x in range(1,100):
    time.sleep(0.3)
    base_url = 'http://auto.gasgoo.com/pvdata/index-{}.html'.format(x)
    wb_data = requests.get(base_url)
    response = urllib.request.urlopen(base_url)
    html = response.read().decode('utf8',errors='replace')
    soup = BeautifulSoup(wb_data.text,'lxml')
    wb_urls = soup.select('div.nebox ul li a')
    for wb_url in wb_urls:
        if '长安汽车' in wb_url.text:
            print(wb_url.get('title'))
            print(wb_url.get('href'))

















'''

jili_url = 'http://auto.gasgoo.com/News/2016/10/18062346234660369834880.shtml'



wb_data = requests.get(jili_url)
response = urllib.request.urlopen(jili_url)
html = response.read().decode('utf8',errors='replace')
soup = BeautifulSoup(html,'lxml')
if soup.title.text.find('吉利'):
    brand = '吉利汽车'
titles = soup.select('tr strong')
datas_1 = soup.select('tr td')
title_all = []
item_all = []
for data_1 in datas_1:
    if data_1.find('strong'):
        title_all.append(data_1)
    else:
        item_all.append(data_1)

title_all_count = len(title_all)
item_all_count = len(item_all)
chexing = title_all[0].text
now_y_m = title_all[1].text
last_y_m = title_all[2].text
tb = title_all[3].text
now_a_m = title_all[4].text
last_a_m = title_all[5].text
y_tb = title_all[6].text

for i in range(0,int(int(item_all_count)/7)):
    car_datas={
        '品牌':brand,
        chexing:item_all[i*7+0].text,
        now_y_m:item_all[i*0+1].text,
        last_y_m:item_all[i*7+2].text,
        tb:item_all[i*7+3].text,
        now_a_m:item_all[i*7+4].text,
        last_a_m:item_all[i*7+5].text,
        y_tb:item_all[i*7+6].text
    }
    print(car_datas)

'''
