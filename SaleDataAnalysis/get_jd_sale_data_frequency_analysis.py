# 对数据进行频数分析

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.family"] = "SimHei"  # 使用支持的黑体中文字体
mpl.rcParams["axes.unicode_minus"] = False  #  用来正常显示负号"-"

plt.rcParams['font.sans-serif'] = ['SimHei']  #  用来正常显示中文标签


# 不同省/自治区销售数据频数分析
def different_regions_sale_data_frequnency_analysis(jd_sale_data):
    table = pd.pivot_table(
        jd_sale_data,
        index=["省/自治区"],
        values=["销售额", "数量", "利润"],
        aggfunc={"销售额": lambda x: np.sum(x)/1000, "利润": lambda x: np.sum(x)/1000, "数量": "count"},
        fill_value=0
    ).sort_values(by="销售额", ascending=False)
    print(table)
    table.plot(kind='bar', width=0.9)
    plt.xticks(fontsize=8, rotation=60)
    plt.xlabel("省/自治区")
    plt.ylabel("数量/额度", rotation=90)
    plt.legend(labels=["利润（千元）", "数量", "销售额（千元）"], loc='upper right', fontsize=10)
    plt.savefig("./不同省及自治区销售数据频数分析柱状图.png", dpi=300)
    plt.show()
