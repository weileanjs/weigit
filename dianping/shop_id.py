import pymongo
import pandas as pd
client = pymongo.MongoClient('localhost',27017)
db = client['dianping']
data = pd.DataFrame(list(db['hz_foods'].find()))
shop_l = list(data['id'])
got = list(pd.DataFrame(list(db['got'].find()))['got'])
now_url_l =list(set(shop_l).difference(set(got))) # b中有而a中没有的
print('剩余:  '+str(len(now_url_l)))

# got_url=[1,2,3]
# for i in got_url:
#     x_dict = {'got':i}
#     db['got'].insert_one(x_dict)
# db['shop_list_raw'].insert_many(shop_l.to_dict('records'))

