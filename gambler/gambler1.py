import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""
    设置100个赌徒
"""
gamblers = 100

"""
    赌场：简单设定每个赌徒一共有1000000一共想在赌场玩10000000次，你要是没钱了也别想玩了
    win_rate:   输赢的概率
    win_once:   每次赢的钱数
    loss_once:  每次输的钱数
    commission: 手续费这里简单的设置了0.01 1%
"""
def casino_nb(win_rate, win_once=1, loss_once=1, commission=0.01):
    my_money = 10000
    play_cnt = 100000
    commission = commission
    for i in np.arange(0, play_cnt):
        w = np.random.binomial(1, win_rate)
        if w:
            my_money += win_once
        else:
            my_money -= loss_once
        my_money -= commission
        if my_money <= 0:
            break
    return my_money
"""
    天堂赌场，没有抽头，没有老千😇
    heaven_moneys 100个
    都去了之后玩回来之后的结果
"""
#heaven_moneys = [casino_nb(0.5, commission=0) for _ in np.arange(0, gamblers)]

# """
#     没有抽头，有老千😫
# """
# moneys_low = [casino_nb(0.4, commission=0) for _ in np.arange(0, gamblers)]
#
# """
#     有抽头，没有老千😫
# """
moneys_commission = [casino_nb(0.5, commission=0.01) for _ in np.arange(0, gamblers)]
#
# """
#     有抽头，有老千😫
# """
# moneys_low_commission = [casino_nb(0.4, commission=0.01) for _ in np.arange(0, gamblers)]
plt.setp(plt.gca().get_xticklabels(), rotation=30)
pd.Series(moneys_commission).hist(bins=30)
plt.show()
