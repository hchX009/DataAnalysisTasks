import random
import pandas as pd
from pandas import DataFrame
# 机器学习库
from sklearn.preprocessing import StandardScaler, MinMaxScaler



def pretreatment_second_hand_data(data):
    # 采用四分点和中点来映射层高
    height_state = {'高': 0.75, '中': 0.5, '低': 0.25}
    pretreatment_data = DataFrame(data)
    # pretreatment_data["price_cor"] = data["price_cor"]
    pretreatment_data["height_state"] = data.height.map(height_state) * data.layers

    # 独热编码
    pretreatment_data = pretreatment_data.join([pd.get_dummies(data.height),
                                                pd.get_dummies(data.dic),
                                                pd.get_dummies(data.addr_district)])
    # 相关系数
    pretreatment_data.corr().dropna(thresh=1).dropna(axis=1, thresh=1).sort_values(by="price_cor")

    pretreatment_data.to_csv("./青羊区二手房数据_预处理.csv", encoding='utf-8-sig')

    return pretreatment_data


def get_data_set(pretreatment_data):
    # 按price_cor排序并重设index
    pretreatment_data = pretreatment_data.sort_values(by="price_cor").reset_index(drop=True)

    # 标准化，使用该类的好处在于可以保存训练集中的参数（均值、方差）直接使用其对象转换测试集数据。
    ss = StandardScaler()

    # 注意不能保留总售价，会出现完全共线性
    # x数据用loc取对应列所有行
    x = ss.fit_transform(pretreatment_data.loc[:, ("area", "year", "chamber", "hall", "layers", "height_state",
                                                   "中", "低", "高", "东北向", "东南向", "东向", "东西向", "北向",
                                                   "南北向", "南向", "西北向", "西南向", "西向", "万家湾", "光华",
                                                   "八宝街", "内光华", "内金沙", "外光华", "外金沙", "天府广场",
                                                   "府南新区", "杜甫草堂", "浣花小区", "石人小区", "苏坡", "草市街",
                                                   "西南财大", "贝森", "长顺街", "顺城街", "骡马市")])
    # y数据用loc取price_cor列所有行
    y = pretreatment_data.loc[:, "price_cor"]

    # 划分训练集与测试集；测试集选取全部数据的20%
    data_set = {}
    train = []
    test = []
    for i in range(pretreatment_data.shape[0]):
        if random.random() > 0.2:
            train.append(i)
        else:
            test.append(i)
    data_set["x_test"] = x[test]
    data_set["x_train"] = x[train]
    data_set["y_test"] = y[test]
    data_set["y_train"] = y[train]

    return data_set
