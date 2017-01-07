# coding:utf8
# 获取集思路的数据
import json
import time
import requests


# 分级A的接口
__funda_url = 'http://www.jisilu.cn/data/sfnew/funda_list/?___t={ctime:d}'

# 分级B的接口
__fundb_url = 'http://www.jisilu.cn/data/sfnew/fundb_list/?___t={ctime:d}'

# 母基接口
__fundm_url = 'https://www.jisilu.cn/data/sfnew/fundm_list/?___t={ctime:d}'

# 分级套利的接口
#__fundarb_url = 'http://www.jisilu.cn/data/sfnew/arbitrage_vip_list/?___t={ctime:d}'

# 集思录登录接口
__jsl_login_url = 'https://www.jisilu.cn/account/ajax/login_process/'

# 集思录 ETF 接口
__etf_index_url = "https://www.jisilu.cn/jisiludata/etf.php?___t={ctime:d}"
# 黄金 ETF , 货币 ETF 留坑,未完成
__etf_gold_url = "https://www.jisilu.cn/jisiludata/etf.php?qtype=pmetf&___t={ctime:d}"
__etf_money_url = "https://www.jisilu.cn/data/money_fund/list/?___t={ctime:d}"

# 集思录QDII接口
__qdii_url = "https://www.jisilu.cn/data/qdii/qdii_list/?___t={ctime:d}"
# 可转债
__cb_url = "https://www.jisilu.cn/data/cbnew/cb_list/?___t={ctime:d}"

# 分级A数据
# 返回的字典格式
# { 150022:
# {'abrate': '5:5',
#  'calc_info': None,
#  'coupon_descr': '+3.0%',
#  'coupon_descr_s': '+3.0%',
#  'fund_descr': '每年第一个工作日定折，无下折，A不参与上折，净值<1元无定折',
#  'funda_amount': 178823,
#  'funda_amount_increase': '0',
#  'funda_amount_increase_rt': '0.00%',
#  'funda_base_est_dis_rt': '2.27%',                       T溢价率
#  'funda_base_est_dis_rt_t1': '2.27%',                    T-1溢价率
#  'funda_base_est_dis_rt_t2': '-0.34%',                    T-2溢价率
#  'funda_base_est_dis_rt_tip': '',
#  'funda_base_fund_id': '163109',
#  'funda_coupon': '5.75',
#  'funda_coupon_next': '4.75',
#  'funda_current_price': '0.783',
#  'funda_discount_rt': '24.75%',
#  'funda_id': '150022',
#  'funda_increase_rt': '0.00%',
#  'funda_index_id': '399001',
#  'funda_index_increase_rt': '0.00%',
#  'funda_index_name': '深证成指',
#  'funda_left_year': '永续',
#  'funda_lower_recalc_rt': '1.82%',
#  'funda_name': '深成指A',
#  'funda_nav_dt': '2015-09-14',
#  'funda_profit_rt': '7.74%',
#  'funda_profit_rt_next': '6.424%',
#  'funda_value': '1.0405',
#  'funda_volume': '0.00',
#  'fundb_upper_recalc_rt': '244.35%',
#  'fundb_upper_recalc_rt_info': '深成指A不参与上折',
#  'last_time': '09:18:22',
#  'left_recalc_year': '0.30411',
#  'lower_recalc_profit_rt': '-',
#  'next_recalc_dt': '<span style="font-style:italic">2016-01-04</span>',
#  'owned': 0,
#  'status_cd': 'N'}
# }


def formatfundajson(fundajson):
    """格式化集思录返回的json数据,以字典形式保存"""
    d = {}
    for row in fundajson['rows']:
        funda_id = row['id']
        cell = row['cell']
        d[funda_id] = cell
    return d
def formatfundbjson(fundbjson):
    """格式化集思录返回的json数据,以字典形式保存"""
    d = {}
    for row in fundbjson['rows']:
        cell = row['cell']
        fundb_id = cell['fundb_id']
        d[fundb_id] = cell
    return d

def funda( fields=[], min_volume=0, min_discount=0, max_discount=0,ignore_nodown=False, forever=False):
    """以字典形式返回分级A数据
    :param fields:利率范围，形如['+3.0%', '6.0%']
    :param min_volume:最小交易量，单位万元
    :param min_discount:最小折价率, 单位%
    :param ignore_nodown:是否忽略无下折品种,默认 False
    :param forever: 是否选择永续品种,默认 False
    """
    # 添加当前的ctime
    __funda_url = 'http://www.jisilu.cn/data/sfnew/funda_list/?___t={}'
    __funda_url =__funda_url.format(int(time.time()))
    # 请求数据
    rep = requests.get(__funda_url)
    # 获取返回的json字符串
    fundajson = json.loads(rep.text)
    # print(fundajson)
    # print(type(fundajson))
    data = formatfundajson(fundajson)
    # 过滤小于指定交易量的数据
    if min_volume:
        data = {k: data[k] for k in data if float(data[k]['funda_volume']) > min_volume}
    if len(fields):
        data = {k: data[k] for k in data if data[k]['coupon_descr_s'] in ''.join(fields)}
    if ignore_nodown:
        data = {k: data[k] for k in data if data[k]['fund_descr'].find('无下折') == -1}
    if forever:
        data = {k: data[k] for k in data if data[k]['funda_left_year'].find('永续') != -1}
    if min_discount:
        data = {k: data[k] for k in data if float(data[k]['funda_base_est_dis_rt'][:-1]) > min_discount}
    if max_discount:
        data = {k: data[k] for k in data if float(data[k]['funda_base_est_dis_rt'][:-1]) < max_discount}
    __funda = data

    return __funda


###################################################################################
def fundb(fields=[], min_volume=0,  max_discount=0, min_discount=0, forever=False):
    """以字典形式返回分级B数据
    :param fields:利率范围，形如['+3.0%', '6.0%']
    :param min_volume:最小交易量，单位万元
    :param min_discount:最小折价率, 单位%
    :param forever: 是否选择永续品种,默认 False
    """
    __fundb_url = 'http://www.jisilu.cn/data/sfnew/fundb_list/?___t={}'
    __fundb_url =__fundb_url.format(int(time.time()))
    # 请求数据
    rep = requests.get(__fundb_url)
    # 获取返回的json字符串
    fundbjson = json.loads(rep.text)
    # 格式化返回的json字符串
    data = formatfundbjson(fundbjson)
    # 过滤小于指定交易量的数据
    if min_volume:
        data = {k: data[k] for k in data if float(data[k]['fundb_volume']) > min_volume}
    if len(fields):
        data = {k: data[k] for k in data if data[k]['coupon_descr_s'] in ''.join(fields)}
    if forever:
        data = {k: data[k] for k in data if data[k]['fundb_left_year'].find('永续') != -1}
    if min_discount:
        data = {k: data[k] for k in data if float(data[k]['fundb_discount_rt'][:-1]) > min_discount}
    if max_discount:
        data = {k: data[k] for k in data if float(data[k]['funda_discount_rt'][:-1]) < max_discount}
    __fundb = data
    return __fundb

###################################################################################


def fundarb(avolume=0, bvolume=0, ptype='price'):
    """登陆集思录
    '160809': {'redeem_fee': '0.5', 'B卖一量': '0.866', '卖一溢价率%': '0.32442', 'apply_fee': '1.2', 'A卖一量': '0.011', 'A:B': '5:5', '估算净值': '1.0172', 'B卖一价': '0.962', 'A卖一价': '1.079'}
    :param jsl_username: 集思录用户名
    :param jsl_password: 集思路登录密码
    :param avolume: A成交额，单位百万
    :param bvolume: B成交额，单位百万
    :param ptype: 溢价计算方式，price=现价，buy=买一，sell=卖一
    """
    __jsl_login_url = 'https://www.jisilu.cn/account/ajax/login_process/'
    s = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    }
    s.headers.update(headers)

    logindata = dict(return_url='http://www.jisilu.cn/',
                     user_name='weileanjs',
                     password='wchsjsl0202',
                     net_auto_login='1',
                     _post_type='ajax')

    rep = s.post(__jsl_login_url, data=logindata)
    __fundarb_url = 'http://www.jisilu.cn/data/sfnew/arbitrage_vip_list/'
    fundarb_url = __fundarb_url
    pdata = dict(avolume=avolume,
                 bvolume=bvolume,
                 ptype=ptype,
                 is_search='1',
                 market=['sh', 'sz'],
                 rp='50')
    # 请求数据
    rep = s.post(fundarb_url, data=pdata)
    # 获取返回的json字符串
    fundajson = json.loads(rep.text)
    data = formatfundajson(fundajson)
    dict1 = {}
    for k in data.keys():
        dict2={}
        dict2['赎回费率'] =data[k][ 'redeem_fee'].split('%')[0]
        dict2['A:B'] =data[k]['abrate']
        dict2['申购费率'] =data[k][ 'apply_fee'].split('%')[0]
        dict2['估算净值'] =data[k][ 'base_est_val']
        dict2['A卖一价'] =data[k][ 'sell1A']
        dict2['A卖一量'] =data[k][ 'sell1_amountA']
        dict2['B卖一价'] =data[k][ 'sell1B']
        dict2['B卖一量'] =data[k][ 'sell1_amountB']
        a_part=int(data[k]['abrate'].split(':')[0])
        b_part=int(data[k]['abrate'].split(':')[1])
        take_price = (float(data[k][ 'sell1A'])*a_part+float(data[k][ 'sell1B'])*b_part)/10
        sell1_yijia=float((take_price-float(data[k][ 'base_est_val']))/float(data[k][ 'base_est_val'])*100)
        dict2['卖一溢价率%'] ='%0.5f'%sell1_yijia
        dict1[k] =dict2
    return dict1

##############################################################################
def yijia_a(min_disc):
    fundm_info=fundarb()
    d1 = funda(min_discount=min_disc)
    dict_min={}
    for k in d1.keys():
        dict_a={}
        m_id=d1[k]['funda_base_fund_id']
        if float(fundm_info[m_id]['卖一溢价率%'])-float(fundm_info[m_id]['申购费率'])>min_disc and int(d1[k]['funda_amount'])>2000:
            dict_a['t日溢价率']=d1[k]['funda_base_est_dis_rt'].split('%')[0]
            #dict_a['t-1日溢价率']=d1[k]['funda_base_est_dis_rt_t1'].split('%')[0]
            #dict_a['t-2日溢价率']=d1[k]['funda_base_est_dis_rt_t1'].split('%')[0]
            dict_a['跟踪指数']=d1[k]['funda_index_name'].split('%')[0]
            dict_a['a份额']=d1[k]['funda_amount']
            m_id=d1[k]['funda_base_fund_id']
            dict_a['申购费率']=fundm_info[m_id]['申购费率']
            dict_min[m_id]=dict_a
    for k,v in zip(dict_min.keys(),dict_min.values()):
        print(('%s'+':'+'%s')%(k,v))
    return dict_min


def zhejia_a(max_disc,anquandian):
    fundm_info=fundarb()
    d1 = funda(max_discount=max_disc)
    dict_max={}
    for k in d1.keys():
        dict_a={}
        m_id=d1[k]['funda_base_fund_id']
        if float(fundm_info[m_id]['卖一溢价率%'])+float(fundm_info[m_id]['赎回费率'])<anquandian and float(fundm_info[m_id]['B卖一量'])>0.5 and float(fundm_info[m_id]['A卖一量'])>1:
            dict_a['t日折价率']=d1[k]['funda_base_est_dis_rt'].split('%')[0]
            dict_a['跟踪指数']=d1[k]['funda_index_name'].split('%')[0]
            dict_a['a份额']=d1[k]['funda_amount']
            dict_a['赎回费率']=fundm_info[m_id]['赎回费率']
            dict_a['A:B']=fundm_info[m_id]['A:B']
            dict_a['卖一折价率%']=fundm_info[m_id]['卖一溢价率%']
            dict_a['A卖一价']=fundm_info[m_id]['A卖一价']
            dict_a['B卖一价']=fundm_info[m_id]['B卖一价']
            dict_max[m_id]=dict_a
    for k,v in zip(dict_max.keys(),dict_max.values()):
        print(('%s'+':'+'%s')%(k,v))

    return dict_max

