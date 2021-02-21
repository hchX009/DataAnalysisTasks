from get_participation_restaurant import *
from get_favour_catering_type import *
from get_analysis_restaurant_data import *
from get_restaurant_sale_num import *


if __name__ == '__main__':
    Excel = xlwt.Workbook()
    purchase_data_sheet = read_purchase_data()
    # write_analysis_purchase_data(Excel, purchase_data_sheet)
    restaurant_data_sheet = read_restaurant_data()
    # write_analysis_restaurant_data(Excel, restaurant_data_sheet)

    print_participation_restaurant_num(purchase_data_sheet)

    print_top5_catering_type(purchase_data_sheet)

    print_top10_restaurant_sale(purchase_data_sheet)

    print('Finished!')