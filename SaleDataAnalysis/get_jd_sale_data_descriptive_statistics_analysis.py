# 对数据进行集中趋势和离散程度分析

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats

plt.rcParams['font.sans-serif'] = ['SimHei']  #  用来正常显示中文标签


def sale_data_descriptive_statistics_analysis(jd_sale_data):
    concentrate_tendency_analysis = jd_sale_data.describe()
    print(concentrate_tendency_analysis)
    concentrate_tendency_analysis.to_csv("./京东超市销售数据的描述性统计分析.csv", encoding='utf-8-sig')


def sale_data_concentration_tendency_analysis(jd_sale_data):
    df_count = jd_sale_data.count().to_frame()  # 非空元素计数
    df_count.columns = ["计数"]
    df_sum = jd_sale_data.sum().to_frame()  # 求和
    df_sum.columns = ["求和"]
    df_mean = jd_sale_data.mean().to_frame()  # 均值
    df_mean.columns = ["均值"]
    df_median = jd_sale_data.median().to_frame()  # 中位数
    df_median.columns = ["中位数"]
    # df_mode = stats.mode(jd_sale_data)[0][0]  # 众数
    # df_mode.columns = ["众数"]
    df_one_quantile = jd_sale_data.quantile(0.25).to_frame()  # 25%分位数
    df_one_quantile.columns = ["25%分位数"]
    df_two_quantile = jd_sale_data.quantile(0.50).to_frame()  # 50%分位数
    df_two_quantile.columns = ["50%分位数"]
    df_three_quantile = jd_sale_data.quantile(0.75).to_frame()  # 75%分位数
    df_three_quantile.columns = ["75%分位数"]

    result = pd.concat([df_count,
                        df_sum,
                        df_mean,
                        df_median,
                        # df_mode,
                        df_one_quantile,
                        df_two_quantile,
                        df_three_quantile],
                       axis=1)

    def to_float(x):
        try:
            res = float(x)
        except Exception:
            res = "NAN"
        return res

    result = result.applymap(lambda x: to_float(x))
    result = result.fillna("NAN")
    print(result)
    result.to_csv("./京东超市销售数据的集中趋势分析.csv", encoding='utf-8-sig')


def sale_data_dispersion_degree_analysis(jd_sale_data):
    jd_sale_data.max() - jd_sale_data.min()  # 极差 = 最大值 - 最小值
    jd_sale_data.std()  # 标准差
    jd_sale_data.mad()  # 平均绝对偏差
    jd_sale_data.quantile(0.75) - jd_sale_data.quantile(0.25)  # 四分位差
    jd_sale_data.std() / jd_sale_data.mean()  # 离散系数

    jd_sale_data.skew()  # 偏度
    jd_sale_data.kurt()  # 峰度
    jd_sale_data.corr()  # 相关系数
    jd_sale_data.cov()  # 协方差矩阵
    print("\n")
