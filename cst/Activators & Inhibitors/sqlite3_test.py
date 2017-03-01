# 导入SQLite驱动:
import sqlite3
import requests
from bs4 import BeautifulSoup
from page_to_sql import page_to_sqlxxxxx
import pandas as pd
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
# conn = sqlite3.connect('Buffers & Dyes.db')
# 创建一个Cursor:
# cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Accept':'text/html, */*; q=0.01',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Accept-Encoding':'gzip, deflate, sdch',
'Connection':'keep-alive',
'Referer':'https://www.cellsignal.com/',
}

def price_page(p_url,num):
    req_p = requests.get(p_url,headers=headers)
    price_l = []
    name_l = []
    size_l = []
    soup_p = BeautifulSoup(req_p.text,'lxml')
    names = soup_p.select('#purchase > tbody > tr > td:nth-of-type(1)')
    sizes = soup_p.select('#purchase > tbody > tr > td:nth-of-type(2)')
    prices = soup_p.select('#purchase > tbody > tr > td:nth-of-type(3)')
    for price in  prices[:num]:
        if '现货查询' in price.text:
            price=str(price.text).replace('现货查询','').strip()
            price_l.append(price)
        else:
            price_l.append(str(price.text).strip())
    for name in  names[:num]:
        name_l.append(name.text.strip())
    for size in  sizes[:num]:
        size_l.append(size.text.strip().replace('\r\n\t\t\t\t\t\t\t\t\t\t\t',''))
    return price_l,name_l,size_l



def item_urls():
    con = sqlite3.connect('')
    item_urls_ = []
    conn = sqlite3.connect('Buffers & Dyes.db')
    sql ="SELECT *  from item_details"
    cursor = conn.execute("SELECT *  from item_details")
    for row in cursor.fetchall():
        category = row[0],
        art_no = row[1],
        name = row[2],
        size = row[3],
        url = row[4],
        storage = row[5],
        price = row[6],
        description = row[7],
        data_sheet = row[8],
        pid = row[9],
        if len(eval(size[0])) < 2:
            category_s = category[0],
            art_no_s = art_no[0],
            name_s = name[0],
            try:
                size_s = list(eval(size[0]).values())[0],
            except IndexError:
                size_s = 'null'
            url_s = url[0],
            storage_s = storage[0],
            try:
                price_s = eval(price[0])[0],
            except IndexError:
                price_s = 'null'
            description_s = description[0],
            data_sheet_s = data_sheet[0],
            pid_s = pid[0],

            # print(size_s,price_s,url_s)
            # print(category_s,art_no_s,name_s,size_s,url_s,storage_s,price_s,description_s,data_sheet_s,pid_s)
            page_to_sqlxxxxx(category_s[0],art_no_s[0],name_s[0],size_s[0],url_s[0],storage_s[0],price_s[0],description_s[0].replace('"',''),data_sheet_s[0],pid_s[0].replace('"',''))
            print(category_s[0],art_no_s[0],name_s[0],size_s[0],url_s[0],storage_s[0],price_s[0],description_s[0].replace('"',''),data_sheet_s[0],pid_s[0].replace('"',''))
        elif len(eval(size[0])) == 2:
            new_item = price_page('http://www.cst-c.com.cn/products/{}.html'.format(art_no[0]),2)
            price_l = new_item[0]
            art_no_l =new_item[1]
            size_l = new_item[2]
            for p,no,s in zip(price_l,art_no_l,size_l):
                category_s = category[0],
                art_no_s = no,
                name_s = name[0],
                size_s = s,
                url_s = url[0],
                storage_s = storage[0],
                price_s = p,
                description_s = description[0],
                data_sheet_s = data_sheet[0],
                pid_s = pid[0],
                print(category_s[0], art_no_s[0], name_s[0], size_s[0], url_s[0], storage_s[0], price_s[0],
                      description_s[0].replace('"', ''), data_sheet_s[0], pid_s[0].replace('"', ''))
                page_to_sqlxxxxx(category_s[0], art_no_s[0], name_s[0], size_s[0], url_s[0], storage_s[0], price_s[0],
                                 description_s[0].replace('"', ''), data_sheet_s[0], pid_s[0].replace('"', ''))


        else:
            pass
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(len(eval(size[0])))
            print(url[0])
            print(eval(size[0]))

    #
    # print(len(category))

    conn.close()

item_urls()