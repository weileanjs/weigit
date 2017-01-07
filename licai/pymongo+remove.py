import pymongo
import pandas as pd
client = pymongo.MongoClient('localhost',27017)
db = client['lufax']
info = db['lu_zhuanr']


data =pd.DataFrame(list(info.find({'date':'2016-12-28'})))
data2 =pd.DataFrame(list(info.find({'date':'2016-12-28'})))
data2.pop('_id')


dup_item = data2.duplicated()
data['dup_item'] = dup_item


an = data.loc[data['dup_item'] ==True]
#print(len(an))
dup_list = [x for x in an['_id'] ]
print(len(dup_list))

for i in dup_list:
    info.delete_one({"_id":i})
    print("_id:",i,'removed')


def remove_pyrecount(info,item):
    data_raw = pd.DataFrame(list(info.find(item)))
    data_duplicated =  pd.DataFrame(list(info.find(item)))
    data_duplicated.pop('_id')
    recount_item = data_duplicated.duplicated()
    data_raw['dup_item'] = recount_item
    get_dup_true = data_raw.loc[data_raw['dup_item'] ==True]
    dup_list = [x for x in get_dup_true['_id'] ]
    print('data_count: ',len(data_raw))
    print('recount_data: ',len(get_dup_true))
    duped_list = []
    for i in dup_list:
        info.delete_one({"_id":i})
        duped_list.append(i)
    print(len(duped_list),'recounted data removed')

item = {}
remove_pyrecount(info,item)
