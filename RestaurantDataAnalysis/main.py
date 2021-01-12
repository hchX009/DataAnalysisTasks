from get_participation_restaurant import *
from get_favour_catering_type import *
from get_analysis_restaurant_data import *


if __name__ == '__main__':
    Excel = xlwt.Workbook()
    purchase_data_sheet = read_purchase_data()
    # write_analysis_purchase_data(Excel, purchase_data_sheet)
    restaurant_data_sheet = read_restaurant_data()
    # write_analysis_restaurant_data(Excel, restaurant_data_sheet)
    print('参与活动的店铺数量：%d' % (get_participation_restaurant(purchase_data_sheet)))
    print(get_sorted_sale_num(purchase_data_sheet))
    print('Finished!')