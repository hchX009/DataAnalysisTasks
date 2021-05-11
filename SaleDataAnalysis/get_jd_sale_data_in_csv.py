# 从csv文件中进行数据清理，得到清理后的数据表

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

sns.set(style="darkgrid")
sns.set(font="SimHei", font_scale=1)


# 读取京东销售相关数据
def read_jd_sale_data():
    jd_sale_data = pd.read_csv("./京东超市销售数据.csv")
    # print(jd_data.head())
    # 数据清洗，将数据中作为千元分割的 "," 去除，并将数字字符串转换为float格式，将利润率和折扣转换为小数
    jd_sale_data[["每笔订单利润", "销售额预测", "每名客户销售额", "利润", "销售额"]] \
        = jd_sale_data[["每笔订单利润", "销售额预测", "每名客户销售额", "利润", "销售额"]]\
        .applymap(lambda x: x.replace(",", "")).astype("float")
    jd_sale_data[["利润率", "折扣"]] \
        = jd_sale_data[["利润率", "折扣"]] \
        .applymap(lambda x: x.replace("%", "")).astype("float") / 100
    return jd_sale_data
