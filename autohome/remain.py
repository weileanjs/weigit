import pymongo
import pandas as pd
client = pymongo.MongoClient('localhost',27017)
db = client['autohome']
ready_url= pd.DataFrame(list(db['ready_url_boyue'].find()))['done'].tolist()
all_ = [i for i in range(1,1001)]
now_url_l =list(set(all_).difference(set(ready_url))) # b中有而a中没有的
print('剩余:  '+str(len(now_url_l)))

# got_url=[1,2,3]
# for i in got_url:
#     x_dict = {'got':i}
#     db['got'].insert_one(x_dict)
# db['shop_list_raw'].insert_many(shop_l.to_dict('records'))

