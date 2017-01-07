
import time
import pandas as pd
import pymongo
import json
import numpy as np
import tushare as ts
client = pymongo.MongoClient('localhost',27017)
db = client['stock_basic_datas']
stock_basics_d = db['bascis']
print(stock_basics_d.find_one({},{"code":1,"esp":1,"_id":0}))
