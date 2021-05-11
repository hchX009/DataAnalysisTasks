from get_jd_sale_data_in_csv import read_jd_sale_data
from get_jd_sale_data_frequency_analysis import *
from get_jd_sale_data_descriptive_statistics_analysis import *
from get_jd_sale_data_correlation_analysis import *


if __name__ == '__main__':
    jd_sale_data = read_jd_sale_data()
    print("\n得到的京东超市销售数据：")
    print(jd_sale_data.head())
    print("\n得到的京东超市销售数据频数分析柱状图：")
    different_regions_sale_data_frequnency_analysis(jd_sale_data)
    print("\n得到的东超市销售数据的集中趋势分析表格：")
    sale_data_concentration_tendency_analysis(jd_sale_data)
    print("\n得到的京东销售数据的两两相关性关系图：")
    sale_data_correlation_analysis(jd_sale_data)
    print("\n得到的京东超市地区和销售额的相关性散点图和小提琴图：")
    sale_data_correlation_analysis_about_sale_and_area(jd_sale_data)
    print("\n得到的京东超市销售对象和物品类别相关性直方图：")
    sale_data_correlation_analysis_about_sale_target_and_object(jd_sale_data)
