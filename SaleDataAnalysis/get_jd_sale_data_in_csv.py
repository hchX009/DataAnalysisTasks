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
    # 数据清洗，将数据中作为千元分割的 "," 去除，并将数字字符串转换为float格式
    jd_sale_data[["每笔订单利润", "销售额预测", "每名客户销售额", "利润", "销售额"]] \
        = jd_sale_data[["每笔订单利润", "销售额预测", "每名客户销售额", "利润", "销售额"]]\
        .applymap(lambda x: x.replace(",", "")).astype("float")
    return jd_sale_data


def something_else():
    # 数值变量的集中趋势和离散趋势
    jd_data["利润率"] = jd_data["利润"] / jd_data["每名客户销售额"]
    jd_data.describe()
    jd_data.corr()


    # 地区和销售额的相关性（散点图和小提琴图表示）
    sns.stripplot(x="地区", y="销售额",
                  data=jd_data, jitter=True,
                  hue="装运状态", dodge=True,
                  palette="Accent")
    plt.show()
    sns.violinplot(x=jd_data["地区"], y=jd_data["销售额"],
                   palette="Greens")
    plt.show()

    # 销售对象和物品类别相关性（直方图表示）
    sns.catplot(x="类别", col="细分",
                data=jd_data, kind="count",
                height=8, aspect=.7,
                palette="Set2")
    plt.show()

    #散点图总集
    sns.pairplot(jd_data, palette="Greens")
    plt.figure(figsize=(40, 40), dpi=150)
    plt.show()