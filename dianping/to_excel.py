import pandas as pd
import numpy as np
import time
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['dianping']
data = pd.DataFrame(list(db['hz_foods'].find()))
data.pop('_id')
print(len(data))
x1 =data.drop_duplicates

print(x1)

#print(x1.shape)

print(type(x1))

