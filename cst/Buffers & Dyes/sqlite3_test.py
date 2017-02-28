# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('Buffers & Dyes.db')
# 创建一个Cursor:
# cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

def item_urls():
    item_urls_ = []
    cursor = conn.execute("SELECT item_url  from item_urls")
    for row in cursor:
        item_urls_.append(row[0])
    tot = list(set(item_urls_))
    print('count:'+str(len(tot)))
    conn.close()
    return tot
print(item_urls())


# 通过rowcount获得插入的行数:

#
# # 关闭Cursor:
# cursor.close()
# # 提交事务:
# conn.commit()
# # 关闭Connection:
# conn.close()
