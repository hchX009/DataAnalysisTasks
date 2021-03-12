# 得到销售Top10的店铺
# 通过根据销售额排序的方式取Top10的店铺输出


def get_sorted_restaurant_sale_num(purchase_data_sheet):
    num = 1
    restaurant_sale_num = {}
    sorted_restaurant_sale_num = {}
    first_restaurant = purchase_data_sheet[0]['店名']
    restaurant_sale_num[first_restaurant] = purchase_data_sheet[0]['购买人数']
    for data in purchase_data_sheet:
        if data['店名'] != first_restaurant:
            num += 1
            first_restaurant = data['店名']
            restaurant_sale_num[first_restaurant] = data['购买人数']
        else:
            restaurant_sale_num[first_restaurant] += data['购买人数']
    for item in sorted(restaurant_sale_num.items(), key=lambda item: item[1], reverse=True):
        sorted_restaurant_sale_num[item[0]] = item[1]
    return sorted_restaurant_sale_num


def print_top10_restaurant_sale(purchase_data_sheet):
    print('\n销售最多的店铺Top10:')
    sorted_restaurant_sale_num = get_sorted_restaurant_sale_num(purchase_data_sheet)
    # print(sorted_restaurant_sale_num)
    i = 0
    for key, value in sorted_restaurant_sale_num.items():
        if i in range(10):
            print('Top %d : ' % (i + 1) + key + ' -> 总人数: %d' % value)
            i += 1
        else:
            break
