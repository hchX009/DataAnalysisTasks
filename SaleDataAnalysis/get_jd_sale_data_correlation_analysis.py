# 对数据进行相关性分析，用小提琴图、直方图以及散点图表示

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

sns.set(style="darkgrid")
sns.set(font="SimHei", font_scale=1)


# 京东销售数据的两两相关性
def sale_data_correlation_analysis(jd_sale_data):
    sns.pairplot(jd_sale_data, hue="地区", palette="Set3")
    plt.savefig("./京东销售数据的两两相关性关系图.png", dpi=150)
    plt.show()


# 地区和销售额的相关性（散点图和小提琴图表示）
def sale_data_correlation_analysis_about_sale_and_area(jd_sale_data):
    sns.stripplot(x="地区", y="销售额",
                  data=jd_sale_data, jitter=True,
                  hue="装运状态", dodge=True,
                  palette="Accent")
    plt.savefig("./不同地区和销售额的相关性散点图.png", dpi=300)
    plt.show()

    sns.violinplot(x="地区", y="销售额",
                   data=jd_sale_data,
                   hue="装运状态",
                   palette="Accent")
    plt.savefig("./不同地区和销售额的相关性小提琴图.png", dpi=300)
    plt.show()


# 销售对象和物品类别相关性（直方图表示）
def sale_data_correlation_analysis_about_sale_target_and_object(jd_sale_data):
    sns.countplot(x="类别", hue="细分",
                  data=jd_sale_data,
                  palette="Set2")
    plt.savefig("./销售对象和物品类别相关性直方图.png", dpi=300)
    plt.show()
