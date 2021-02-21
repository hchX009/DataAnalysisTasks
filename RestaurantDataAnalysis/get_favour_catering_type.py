# 得到top5受欢迎的餐饮类型
# 将团购活动的购买人数依次排序输出，得到一个按购买人数从高到低排列的 <团购名, 购买人数> 序列
# 通过排列的 <团购名, 购买人数> 序列和自定义的餐饮类型，匹配得到每种餐饮类型的总购买人数
# 通过排序后的每种餐饮类型的总购买人数序列，得到top5受欢迎的餐饮类型


def get_sorted_sale_num(purchase_data_sheet):
    sale_num = {}
    sorted_sale_num = {}
    for data in purchase_data_sheet:
        sale_num[data['团购名']] = int(data['购买人数'])
    for item in sorted(sale_num.items(), key=lambda item: item[1], reverse=True):
        sorted_sale_num[item[0]] = item[1]
    return sorted_sale_num


def get_favour_catering_type(sorted_sale_num):
    types = ['自助', '串串', '火锅', '烧肉', '涮', '鸡公煲', '烧烤', '鱼', '海鲜']
    type_sale_num = {}
    sorted_type_sale_num = {}
    for catering_type in types:
        type_sale_num[catering_type] = 0
    for data in sorted_sale_num:
        for catering_type in types:
            if catering_type in data:
                type_sale_num[catering_type] += sorted_sale_num[data]
    for item in sorted(type_sale_num.items(), key=lambda item: item[1], reverse=True):
        sorted_type_sale_num[item[0]] = item[1]
    return sorted_type_sale_num


def print_top5_catering_type(purchase_data_sheet):
    print('\ntop5受欢迎的餐饮类型:')
    sorted_type_sale_num = get_favour_catering_type(get_sorted_sale_num(purchase_data_sheet))
    i = 0
    for key, value in sorted_type_sale_num.items():
        if i in range(5):
            print('Top %d : ' % (i + 1) + key + ' -> 总人数: %d' % value)
            i += 1
        else:
            break
