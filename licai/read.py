import datetime
from bs4 import BeautifulSoup
import urllib
import pandas as pd
import numpy as np
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
db = client['lufax']
# # db['lu_zhuanr'].remove({'date':'2016-12-17'})
data = pd.DataFrame(list(db['lu_zhuanr'].find({'date':'2016-12-17'})))
print(data)
