import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def show_good_restaurant_num_with_area(restaurant_data_sheet):
    good_restaurant_num_with_area = {}
    for data in restaurant_data_sheet:
        if data['行政区'] not in good_restaurant_num_with_area.keys():
            good_restaurant_num_with_area[data['行政区']] = 0
        if data['评分'] >= 4:
            good_restaurant_num_with_area[data['行政区']] += 1
    y = good_restaurant_num_with_area
    x = np.arange(len(y.keys()))
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    plt.bar(x, height=y.values(), align='center', color='green', width=0.5)
    plt.xticks(x, y.keys(), size='small', rotation=60)
    for a, b in zip(x, y.values()):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
    plt.show()
    #print(good_restaurant_num_with_area)
    return