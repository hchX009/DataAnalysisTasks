import xlrd  # xlrd 2.0.1版本只支持.xls文件,需要安装1.2.0版本（pip install xlrd==1.2.0）
import xlwt
import re


def read_purchase_data():
    sheet = xlrd.open_workbook('./餐饮团购活动.xlsx').sheet_by_name('Sheet1')
    sheet_rows = sheet.nrows
    new_sheet = []
    for row in range(1, sheet_rows):
        sheet_row_dict = {}
        sheet_row_dict['团购名'] = sheet.cell(row, 0).value
        sheet_row_dict['店名'] = sheet.cell(row, 1).value
        sheet_row_dict['购买人数'] = sheet.cell(row, 4).value
        evaluation = sheet.cell(row, 5).value
        if evaluation == '暂无评价':
            sheet_row_dict['团购评价'] = ''
        else:
            sheet_row_dict['团购评价'] = evaluation
        discount_value = sheet.cell(row, 8).value
        market_value = sheet.cell(row, 9).value
        if discount_value == '' or market_value == '':
            discount_info = sheet.cell(row, 3).value
            discount_value = re.search(r'仅售(.*?)元', discount_info).group(1)
            market_value = re.search(r'价值(.*?)元', discount_info).group(1)
        sheet_row_dict['团购价'] = discount_value
        sheet_row_dict['市场价'] = market_value
        new_sheet.append(sheet_row_dict)
        print(sheet_row_dict)
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
        sheet_row_dict['评分'] = sheet.cell(row, 3).value
        new_sheet.append(sheet_row_dict)
        print(sheet_row_dict)
    return new_sheet


def write_analysis_purchase_data():
    return


def write_analysis_restaurant_data():
    return


if __name__ == '__main__':
    read_restaurant_data()
