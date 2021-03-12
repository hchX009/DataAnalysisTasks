# 得到团购优惠的额度(折扣)与店铺活动销售关系
# 展示其团购优惠的额度和购买数量散点图
# 计算团购优惠的额度和购买数量皮尔逊积矩相关系数

import pandas as pd  # 数据处理库
import matplotlib as mpl  # 画图基础库
import matplotlib.pyplot as plt  # 最常用的绘图库

mpl.rcParams["font.family"] = "SimHei"  # 使用支持的黑体中文字体
mpl.rcParams["axes.unicode_minus"] = False  #  用来正常显示负号"-"
plt.rcParams['font.sans-serif'] = ['SimHei']  #  用来正常显示中文标签


def get_discount_relationship_with_sale_num(purchase_data_sheet):
    result = {}
    discounts = []
    sale_nums = []
    for data in purchase_data_sheet:
        discount = data['团购价'] / data['市场价']
        sale_num = data['购买人数']
        discounts.append(discount)
        sale_nums.append(sale_num)
    result["discounts"] = discounts
    result["sale_nums"] = sale_nums
    return result


def show_discount_and_sale_num_scatter_graph(discounts, sale_nums):
    plt.scatter(discounts, sale_nums, marker=".")  # 绘制散点图
    plt.xlim(xmax=1, xmin=0)
    plt.ylim(ymax=5000, ymin=0)
    plt.title("团购优惠的额度和购买数量散点图")
    plt.xlabel("团购优惠的额度")
    plt.ylabel("购买数量")
    plt.savefig("./团购优惠的额度和购买数量散点图.png")
    plt.show()


def compute_PPMCC_with_discount_and_sale_num(result):
    # 皮尔逊积矩相关系数(PPMCC)的取值范围为[-1, 1]。当接近1时，表示两者具有强烈的正相关性；当接近-1时，表示有强烈的的负相关性。
    # 而若值接近0，则表示相关性很低。
    # 相关系数还有 Kendall Tau correlation coefficient 和 Spearman rank correlation 两种
    df = pd.DataFrame(result)
    print("\n团购优惠的额度和购买数量皮尔逊积矩相关系数：")
    print("团购优惠的额度和购买数量相关系数矩阵：")
    corr_matrix = df.corr()
    print(corr_matrix)
    print("团购优惠的额度和购买数量的相关系数：%f" % corr_matrix["discounts"]["sale_nums"])
    print("团购优惠的额度和购买数量相关系数接近0，相关性低，团购优惠的额度和购买数量不具有相关性")
