import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import re
import lxml
import time
import os
from multiprocessing import Pool
import pymssql
# proxies = {"http": "http://111.124.205.31:80","https": "https://111.124.205.31:80"}

# client = pymongo.MongoClient('localhost',27017)
db = 'siRNA.db'
table = 'item_urls'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
'Accept':'text/html, */*; q=0.01',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Accept-Encoding':'gzip, deflate, sdch',
'Connection':'keep-alive',
'Referer':'https://www.cellsignal.com/',
}
base_url = 'https://www.cellsignal.com/browse/sirna?N=102302+4294956287&No=0&Nrpp=200'



def get_urls():
    req = requests.get(base_url,headers=headers)
    soup = BeautifulSoup(req.text,'lxml')
    urls = soup.select(' tr > td > a')
    li = []
    for i in urls:
        li.append('https://www.cellsignal.com'+i.get('href'))
    li_ =list(set(li))
    print(len(li_))
    url_pd = pd.DataFrame({'item_url':li_})
    # info.insert_many(url_pd.to_dict('records'))                  #mongodb

    conn = sqlite3.connect(db)
    print("Opened "+db+" successfully")
    conn.execute('DROP TABLE IF EXISTS "table"')
    try:
        conn.execute('''CREATE TABLE '''+table+'''
               (item_url       text)''')
    except :pass
    for url in li_:
        sql = "INSERT INTO {} (item_url) VALUES ({})".format(table,'\''+url+'\'')
        print(sql)
        conn.execute(sql)
        conn.commit()
    conn.close()
get_urls()




    # cur = conn.cursor()
    # insertSql = "insert into dbo.sta(a,b,c) values(%s,'%s‘,'%s')" %(1,2,3)
    # cur.execute(insertSql)




'''
    *****************************sql**********************
    conn=pymssql.connect(host='127.0.0.1:2301',user = 'sa',password = 'wch900202',database="cst")
    cursor=conn.cursor()
    cursor.execute("""
    IF OBJECT_ID('item_urls') IS NOT NULL
    DROP TABLE item_urls
    CREATE TABLE item_urls (
    item_url VARCHAR(1000),
    )
    """)
    cursor.executemany( "INSERT INTO item_urls VALUES (%s)",li_)
    conn.commit()
    print(str(len(li_))+' is done')
'''
