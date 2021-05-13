# 从csv文件中进行数据清理，得到清理后的数据表
import re
import pandas as pd
import seaborn as sns

sns.set(style="darkgrid")
sns.set(font="SimHei", font_scale=1)


def read_second_hand_housing_data():
    qyq_second_hand_housing_data = pd.read_csv("./青羊区二手房.csv",
                                               names=["title", "room", "area", "height",
                                                      "dic", "year", "addr", "cost", "price"],
                                               encoding='GB18030'
                                               )
    # 数据清洗
    # 删去包含null的行
    qyq_second_hand_housing_data.dropna(axis=0, how='any', inplace=True)
    # 去除换行符和制表符
    qyq_second_hand_housing_data.title = qyq_second_hand_housing_data.title.apply(
        lambda x: x.replace("\t", "").replace("\n", ""))
    # 将别墅区的房屋信息去除
    qyq_second_hand_housing_data = qyq_second_hand_housing_data.drop(
        qyq_second_hand_housing_data[
            (qyq_second_hand_housing_data['room'] == "独栋") |
            (qyq_second_hand_housing_data['room'] == "联排") |
            (qyq_second_hand_housing_data['room'] == "双拼") |
            (qyq_second_hand_housing_data['room'] == "叠加")]
        .index)
    # print(qyq_second_hand_housing_data)
    qyq_second_hand_housing_data["chamber"] = qyq_second_hand_housing_data.room.apply(lambda x: int(x[0]))
    qyq_second_hand_housing_data["hall"] = qyq_second_hand_housing_data.room.apply(lambda x: int(x[2]))
    # qyq_second_hand_housing_data.head()
    # 研究非别墅区，提取数字，处理定性变量
    data = qyq_second_hand_housing_data.sort_values(
        by="area", axis=0,
        ascending=True, inplace=False,
        kind='quicksort', na_position='last')
    # data["chamber"] = data.chamber
    # data["hall"] = data.hall
    # 转换面积为浮点数
    data["area"] = data.area.apply(lambda x: x.replace("㎡", "")).astype("float")
    # 转换层数为浮点数
    data["layers"] = data.height.apply(lambda x: int(x.split("（共")[-1][:-2]))
    # 判断为高层还是低层
    data["height"] = data.height.apply(lambda x: x[0])
    # 提取年份
    data["year"] = data.year.apply(lambda x: int(re.findall(r"\d+\.?\d*", x)[0]))
    # 得到地址和详细地址
    data["addr_district"] = data.addr.apply(lambda x: x.split("-")[0])
    data["addr_detail"] = data.addr.apply(lambda x: x.split("-")[-1])
    # 将开销转换为浮点数
    data["cost"] = data.cost.astype("float")
    # 提取价格
    data["price"] = data.price.apply(lambda x: int(re.findall(r"\d+\.?\d*", x)[0]))
    data["price_cor"] = data.cost / data.area * 10000

    # 去除不需要的行
    data.drop(labels='addr', axis=1, inplace=True)
    data.drop(labels='room', axis=1, inplace=True)

    data.to_csv("./青羊区二手房数据_已清洗.csv", encoding='utf-8-sig')

    return data
