import pandas as pd

import sqlite3
import re

db = 'siRNA.db'
table = 'item_details'

def page_to_sql3(category,art_no,name,size,url,storage,price,description, data_sheet,pid):
    conn = sqlite3.connect(db)
    try:
        conn.execute('''CREATE TABLE '''+table+'''
            (category       CHAR(256),
             art_no        CHAR(256),
             name          CHAR(256),
             size          CHAR(256),
             url           CHAR(256),
             storage       CHAR(256),
             price         CHAR(256),
             description   CHAR(256),
             data_sheet    CHAR(256),
             pid           TEXT)''')
    except:pass
    sql = "INSERT INTO {} (category,art_no,name,size,url,storage,price,description, data_sheet,pid) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(table,category,art_no,name,size,url,storage,price,description, data_sheet,pid)
    conn.execute(sql)
    conn.commit()
    conn.close()
    print('save')
# page_to_sql3()

def saved_urls(url):
    conn = sqlite3.connect(db)
    try:
        conn.execute('''CREATE TABLE saved_urls
            (url       CHAR(256))''')
    except sqlite3.OperationalError:
        pass
    sql = "INSERT INTO saved_urls (url) VALUES (\"{}\")".format(url)
    conn.execute(sql)
    conn.commit()
    conn.close()

def err_urls(url,e):
    conn = sqlite3.connect(db)
    try:
        conn.execute('''CREATE TABLE err_urls
            (url       CHAR(256),
             err        CHAR(256))
            ''')
    except sqlite3.OperationalError as er:
        pass
    sql = "INSERT INTO err_urls (url,err) VALUES (\"{}\",\"{}\")".format(url,e)
    conn.execute(sql)
    conn.commit()
    conn.close()


def item_urls():
    item_urls_ = []
    conn = sqlite3.connect(db)
    cursor = conn.execute("SELECT item_url  from item_urls")
    for row in cursor:
        item_urls_.append(row[0])
    tot = list(set(item_urls_))
    conn.close()
    return tot



def s_urls():
    item_urls_ = []
    conn = sqlite3.connect(db)
    cursor = conn.execute("SELECT url from item_details")
    for row in cursor:
        item_urls_.append(row[0])
    s_urls_ = list(set(item_urls_))
    conn.close()
    return s_urls_

def er_urls():
    item_urls_ = []
    conn = sqlite3.connect(db)
    cursor = conn.execute("SELECT url  from err_urls")
    for row in cursor:
        item_urls_.append(row[0])
    er_urls_ = list(set(item_urls_))
    conn.close()
    return er_urls_

def del_url(u):
    conn = sqlite3.connect(db)
    cursor = conn.execute(("DELETE from err_urls where url=\"{}\";").format(u))
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)


# del_url('https://www.cellsignal.com/products/')
#
# err_urls('https://www.cellsignal.com/products/',2222)


#       'category:',category,
#       'art_no:',art_no,
#       'name:',name,
#       'size:',size,
#       'url:',url,
#       'storage:',storage,
#       'price:',price,
#       'description:',description,
#       'data_sheet:',data_sheet,
#       'pid',pid)


def page_to_sqlxxxxx(category,art_no,name,size,url,storage,price,description, data_sheet,pid):
    conn = sqlite3.connect(db)
    try:
        conn.execute('''CREATE TABLE  xxxxx
            (category       CHAR(256),
             art_no        CHAR(256),
             name          CHAR(256),
             size          CHAR(256),
             url           CHAR(256),
             storage       CHAR(256),
             price         CHAR(256),
             description   CHAR(256),
             data_sheet    CHAR(256),
             pid           TEXT)''')
    except:pass
    sql = "INSERT INTO xxxxx (category,art_no,name,size,url,storage,price,description, data_sheet,pid) VALUES (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(category,art_no,name,size,url,storage,price,description, data_sheet,pid)
    conn.execute(sql)
    conn.commit()
    conn.close()
    print('save')
