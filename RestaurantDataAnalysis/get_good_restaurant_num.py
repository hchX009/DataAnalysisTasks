# 得到不同行政区域，口碑良好（选择评分大于4分）的商家数量
# 使用柱状图显示

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["font.family"] = "SimHei"  # 使用支持的黑体中文字体
mpl.rcParams["axes.unicode_minus"] = False  #  用来正常显示负号"-"
plt.rcParams['font.sans-serif'] = ['SimHei']  #  用来正常显示中文标签


def get_good_restaurant_num_with_area(restaurant_data_sheet):
    good_restaurant_num_with_area = {}
    for data in restaurant_data_sheet:
        if data['行政区'] not in good_restaurant_num_with_area.keys():
            good_restaurant_num_with_area[data['行政区']] = 0
        if data['评分'] > 4:
            good_restaurant_num_with_area[data['行政区']] += 1
    # print(good_restaurant_num_with_area)
    return good_restaurant_num_with_area


def show_bar_chart_good_restaurant_num_with_area(y):
    x = np.arange(len(y.keys()))
    plt.bar(x, height=y.values(), align='center', color='green', width=0.5)  # 绘制柱状图
    plt.xticks(x, y.keys(), size='small', rotation=60)  # 柱状图底部坐标轴变名
    # 设置数字标签
    for a, b in zip(x, y.values()):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
    plt.title("不同行政区域，口碑良好（选择评分大于4分）的商家数量柱状图")
    plt.xlabel("行政区域")
    plt.ylabel("商家数量")
    plt.savefig("./不同行政区域，口碑良好（选择评分大于4分）的商家数量柱状图.png")
    plt.show()
