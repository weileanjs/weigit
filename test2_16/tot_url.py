import pandas as pd
tot = []
e1 = pd.read_csv('1-6000.csv')['item_url'].tolist()
e2 = pd.read_csv('7001-.csv')['item_url'].tolist()
e3 = pd.read_csv('err.csv')['item_url'].tolist()


tot.extend(e1)
tot.extend(e2)
tot.extend(e3)
print(len(tot))
print(len(set(tot)))
