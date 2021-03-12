import xlwt
from get_participation_restaurant import *
from get_favour_catering_type import *
from get_analysis_restaurant_data import *
from get_restaurant_sale_num import *
from get_discount_relationship import *
from get_good_restaurant_num import *


if __name__ == '__main__':
    # 从表中得到数据
    Excel = xlwt.Workbook()
    purchase_data_sheet = read_purchase_data()
    # write_analysis_purchase_data(Excel, purchase_data_sheet)
    restaurant_data_sheet = read_restaurant_data()
    # write_analysis_restaurant_data(Excel, restaurant_data_sheet)

    # 显示参加了团购活动的店铺
    print_participation_restaurant_num(purchase_data_sheet)

    # 显示最受消费者喜爱的Top5餐饮类型
    print_top5_catering_type(purchase_data_sheet)

    # 显示销售最多的店铺Top10
    print_top10_restaurant_sale(purchase_data_sheet)

    # 处理团购优惠的额度是否和购买数量存在的关系(散点图，相关系数)
    result = get_discount_relationship_with_sale_num(purchase_data_sheet)
    show_discount_and_sale_num_scatter_graph(result["discounts"], result["sale_nums"])
    compute_PPMCC_with_discount_and_sale_num(result)

    # 显示不同行政区域，口碑良好（选择评分大于4分）的商家数量柱状图
    result = get_good_restaurant_num_with_area(restaurant_data_sheet)
    show_bar_chart_good_restaurant_num_with_area(result)

    print('\nFinished!')