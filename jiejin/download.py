import tushare as ts
scz = ts.get_h_data('399106', index=True,start='2000-01-01', end='2016-12-01')
szzz = ts.get_h_data('000001', index=True,start='2000-01-01', end='2016-12-01')
scz.to_csv(r'D:\W\python\data_history\day\raw_data\sz.csv')
szzz.to_csv(r'D:\W\python\data_history\day\raw_data\sh.csv')

