import xlrd  # xlrd 2.0.1版本只支持.xls文件,需要安装1.2.0版本（pip install xlrd==1.2.0）
import re


def read_purchase_data():
    sheet = xlrd.open_workbook('./餐饮团购活动.xlsx').sheet_by_name('Sheet1')
    sheet_rows = sheet.nrows
    new_sheet = []
    for row in range(1, sheet_rows):
        sheet_row_dict = {}
        sheet_row_dict['团购名'] = sheet.cell(row, 0).value
        sheet_row_dict['店名'] = sheet.cell(row, 1).value
        sheet_row_dict['购买人数'] = int(sheet.cell(row, 4).value)
        evaluation = sheet.cell(row, 5).value
        if evaluation == '暂无评价':
            sheet_row_dict['团购评价'] = 0
        else:
            sheet_row_dict['团购评价'] = float(evaluation)
        discount_value = sheet.cell(row, 8).value
        market_value = sheet.cell(row, 9).value
        if discount_value == '' or market_value == '':
            discount_info = sheet.cell(row, 3).value
            discount_value = re.search(r'仅售(.*?)元', discount_info).group(1)
            market_value = re.search(r'价值(.*?)元', discount_info).group(1)
        sheet_row_dict['团购价'] = float(discount_value)
        sheet_row_dict['市场价'] = float(market_value)
        new_sheet.append(sheet_row_dict)
        # print(sheet_row_dict)
    return new_sheet


def read_restaurant_data():
    sheet = xlrd.open_workbook('./餐饮团购店铺.xlsx').sheet_by_name('Sheet1')
    sheet_rows = sheet.nrows
    new_sheet = []
    for row in range(1, sheet_rows):
        sheet_row_dict = {}
        sheet_row_dict['店名'] = sheet.cell(row, 0).value
        sheet_row_dict['关键词'] = sheet.cell(row, 1).value
        address = sheet.cell(row, 6).value
        if address == '':
            continue
        city = re.search(r'(.*?)市', address).group(1)
        area = re.search(r'市(.*?)(区|县|市|其他)', address).group(1)
        if area == '':
            area = '其他'
        else:
            area = area + address[re.search(r'市(.*?)(区|县|市|其他)', address).span()[1] - 1]
        sheet_row_dict['城市'] = city
        sheet_row_dict['行政区'] = area
        sheet_row_dict['评分'] = float(sheet.cell(row, 3).value)
        new_sheet.append(sheet_row_dict)
        # print(sheet_row_dict)
    return new_sheet


def write_analysis_purchase_data(Excel, new_sheet):
    sheet = Excel.add_sheet('Sheet1')
    sheet.write(0, 0, '店名')
    sheet.write(0, 1, '团购名')
    sheet.write(0, 2, '购买人数')
    sheet.write(0, 3, '团购评价')
    sheet.write(0, 4, '团购价')
    sheet.write(0, 5, '市场价')
    row = 1
    for sheet_row in new_sheet:
        sheet.write(row, 0, sheet_row['店名'])
        sheet.write(row, 1, sheet_row['团购名'])
        sheet.write(row, 2, sheet_row['购买人数'])
        sheet.write(row, 3, sheet_row['团购评价'])
        sheet.write(row, 4, sheet_row['团购价'])
        sheet.write(row, 5, sheet_row['市场价'])
        row += 1
    Excel.save('餐饮团购数据整理.xls')
    return


def write_analysis_restaurant_data(Excel, new_sheet):
    sheet = Excel.add_sheet('Sheet2')
    sheet.write(0, 0, '店名')
    sheet.write(0, 1, '关键词')
    sheet.write(0, 2, '城市')
    sheet.write(0, 3, '行政区')
    sheet.write(0, 4, '评分')
    row = 1
    for sheet_row in new_sheet:
        sheet.write(row, 0, sheet_row['店名'])
        sheet.write(row, 1, sheet_row['关键词'])
        sheet.write(row, 2, sheet_row['城市'])
        sheet.write(row, 3, sheet_row['行政区'])
        sheet.write(row, 4, sheet_row['评分'])
        row += 1
    Excel.save('餐饮团购数据整理.xls')
    return