import matplotlib.pyplot as plt


def show_discount_relationship_with_sale_num(purchase_data_sheet):
    discounts = []
    sale_nums = []
    for data in purchase_data_sheet:
        discount = data['团购价'] / data['市场价']
        sale_num = data['购买人数']
        discounts.append(discount)
        sale_nums.append(sale_num)
    plt.xlim(xmax=1, xmin=0)
    plt.ylim(ymax=5000, ymin=0)
    plt.plot(discounts, sale_nums, '.')
    plt.show()
    return
