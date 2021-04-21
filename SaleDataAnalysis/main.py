from get_jd_sale_data_in_csv import read_jd_sale_data
from get_jd_sale_data_frequency_analysis import *


if __name__ == '__main__':
    jd_sale_data = read_jd_sale_data()
    print("得到的京东超市销售数据：")
    print(jd_sale_data.head())
    different_regions_sale_data_frequnency_analysis(jd_sale_data)