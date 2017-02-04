import pymongo
import pandas as pd
client = pymongo.MongoClient('localhost',27017)
db = client['autohome']
info = db['h6']

def remove_pyrecount(info,item):
    data_raw = pd.DataFrame(list(info.find(item)))
    data_duplicated = pd.DataFrame(list(info.find(item)))
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
