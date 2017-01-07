import pymongo
import pandas as pd
import numpy as np
client = pymongo.MongoClient('localhost',27017)
db = client['dianping']
info = db['hz_foods']
data =pd.DataFrame(list(info.find()))
data.pop('_id')
d1 = data.loc[(data["priceText"] !='')&(data["shopPower"] != 0 )& (data["priceText"] !='5元/小时')]
d1[['priceText']]=d1[['priceText']].astype(np.int32)
#d1[['口味','服务','环境']]=d1[['口味','服务','环境']].astype(np.float)
print(d1.dtypes)
