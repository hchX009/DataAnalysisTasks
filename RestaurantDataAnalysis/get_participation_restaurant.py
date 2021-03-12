# 统计参加活动的餐馆


def get_participation_restaurant(purchase_data_sheet):
    num = 1
    first_restaurant = purchase_data_sheet[0]['店名']
    for data in purchase_data_sheet:
        if data['店名'] != first_restaurant:
            num += 1
            first_restaurant = data['店名']
    return num


def print_participation_restaurant_num(purchase_data_sheet):
    print("\n参与活动的店铺数量：%d" % (get_participation_restaurant(purchase_data_sheet)))
