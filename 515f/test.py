# import re
# ttt = '<title>2016年12月国产SUV销量排行榜1-96名完整版_汽车销量排行榜_515汽车排行网</title>'
# pattern = re.compile(r'.*2016年\d+月国产SUV销量排行榜.*')
# # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
# match = pattern.match(ttt)
#
# if match:
#     # 使用Match获得分组信息
#     print (match.group())
# else:
#     print('xxx')

import pymongo
import pandas as pd
client = pymongo.MongoClient('localhost',27017)
db = client['515f']
info = db['zz_suv']



info.delete_one({'_id':'589c5074fa30742a98dc30b7'})
data_raw = info.find({},{'_id':1})
print(data_raw)
