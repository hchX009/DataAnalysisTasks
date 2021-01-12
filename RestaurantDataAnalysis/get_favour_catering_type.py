# 得到top5受欢迎的餐饮类型
# 将团购活动的购买人数依次排序输出，得到一个按购买人数从高到低排列的 <团购名, 购买人数> 序列


def get_sorted_sale_num(purchase_data_sheet):
    sale_num = {}
    sorted_sale_num = {}
    for data in purchase_data_sheet:
        sale_num[data['团购名']] = int(data['购买人数'])
    for item in sorted(sale_num.items(), key=lambda item: item[1], reverse=True):
        sorted_sale_num[item[0]] = item[1]
    return sorted_sale_num


def get_favour_catering_type(sorted_sale_num):
    types = ['自助', '火锅', '烧肉', '涮', '鸡公煲', '烧烤', '鱼', '海鲜', '虾', '单人', '双人']
    return
