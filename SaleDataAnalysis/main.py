import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

sns.set(font="SimHei", font_scale=1)

pd.set_option("max_rows", None)
pd.set_option("max_columns", None)

# 京东超市销售数据分析
def jd_data():
    # 获取数据
    jd_data = pd.read_csv("./京东超市销售数据.csv")
    jd_data.head()
    jd_data[["每笔订单利润", "销售额预测", "每名客户销售额", "利润", "销售额"]] \
        = jd_data[["每笔订单利润", "销售额预测", "每名客户销售额", "利润", "销售额"]]\
        .applymap(lambda x: x.replace(",", "")).astype("float")

    # 数值变量的集中趋势和离散趋势
    jd_data["利润率"] = jd_data["利润"] / jd_data["每名客户销售额"]
    jd_data.describe()
    jd_data.corr()

    # 销售额和利润率频数分析
    pd.pivot_table(jd_data,
                   index=["地区"],
                   values=["销售额"],
                   aggfunc={"销售额": [np.max, np.mean]}
                   ).plot(kind='barh')
    pd.pivot_table(jd_data,
                   index=["地区"],
                   values=["利润率"],
                   aggfunc={"利润率": [np.max, np.mean]}
                   ).plot(kind='barh')
    plt.show()

    # 地区和销售额的相关性（散点图和小提琴图表示）
    sns.stripplot(x="地区", y="销售额",
                  data=jd_data, jitter=True,
                  hue="装运状态", dodge=True,
                  palette="Accent")
    plt.show()
    sns.violinplot(x=jd_data["地区"], y=jd_data["销售额"],
                   palette="Greens")
    plt.show()

    # 销售对象和物品类别相关性（直方图表示）
    sns.catplot(x="类别", col="细分",
                data=jd_data, kind="count",
                height=8, aspect=.7,
                palette="Set2")
    plt.show()

    #散点图总集
    sns.pairplot(jd_data, palette="Greens")
    plt.figure(figsize=(40, 40), dpi=150)
    plt.show()

if __name__ == '__main__':
    # 数据读取
    qyq_house_data = pd.read_csv("./青羊区二手房.csv",
                                 names=["title", "room", "area", "height", "dic", "year", "addr", "cost", "price"],
                                 encoding='gbk')
    # 删去空行
    qyq_house_data.dropna(axis=0, how='any', inplace=True)
    # 去除换行符和制表符
    qyq_house_data.title = qyq_house_data.title.apply(lambda x: x.replace("\t", "").replace("\n", ""))
    qyq_house_data.head()

    qyq_house_data.room = qyq_house_data.room.apply(lambda x: [x, "d室d厅"][x == "独栋"])
    qyq_house_data.room = qyq_house_data.room.apply(lambda x: [x, "l室l厅"][x == "联排"])
    qyq_house_data.room = qyq_house_data.room.apply(lambda x: [x, "s室s厅"][x == "双拼"])
    qyq_house_data.room = qyq_house_data.room.apply(lambda x: [x, "j室j厅"][x == "叠加"])
    print(qyq_house_data.room.apply(lambda x: x))
    qyq_house_data["room"] = qyq_house_data.room.apply(lambda x: x[0])
    qyq_house_data["hall"] = qyq_house_data.room.apply(lambda x: x[2])

    # 研究非别墅区,提取数字,处理定性变量
    normal_house = qyq_house_data.sort_values(by="area", axis=0,
                                              ascending=True, inplace=False,
                                              kind='quicksort', na_position='last'
                                              ).head(-103)

    normal_house["room"] = normal_house.room.apply(lambda x: int(x[0]))
    normal_house["hall"] = normal_house.room.apply(lambda x: int(x[2]))
    normal_house["area"] = normal_house.area.apply(lambda x: x.replace("㎡", "")).astype("float")
    normal_house["layers"] = normal_house.height.apply(lambda x: int(x.split("（共")[-1][:-2]))
    normal_house["height"] = normal_house.height.apply(lambda x: x[0])
    normal_house["year"] = normal_house.year.apply(lambda x: int(re.findall(r"\d+\.?\d*", x)[0]))
    normal_house["addr_1"] = normal_house.addr.apply(lambda x: x.split("-")[0])
    normal_house["addr_2"] = normal_house.addr.apply(lambda x: x.split("-")[-1])
    normal_house["cost"] = normal_house.cost.astype("float")
    normal_house["price"] = normal_house.price.apply(lambda x: int(re.findall(r"\d+\.?\d*", x)[0]))
    normal_house["price_cor"] = normal_house.cost / normal_house.area * 10000

    # 采用四分点和中点来映射层高
    height_state = {'高': 0.75, '中': 0.5, '低': 0.25}
    normal_house["height_state"] = normal_house.height.map(height_state) * normal_house.layers

    # 独热编码
    normal_house = normal_house.join([pd.get_dummies(normal_house.height), pd.get_dummies(normal_house.dic), pd.get_dummies(normal_house.addr_1)])
    normal_house.head(1)

    # 相关系数
    normal_house.corr().dropna(thresh=1).dropna(axis=1, thresh=1).sort_values(by="price_cor")

    #数据集划分与标准化
    from sklearn.preprocessing import StandardScaler, MinMaxScaler
    from sklearn.metrics import *
    from sklearn.linear_model import LinearRegression
    from sklearn.svm import SVR
    import random
    scaler = StandardScaler()
    mms = MinMaxScaler()

    normal_house = normal_house.sort_values(by="price_cor").reset_index(drop=True)
    # 注意不能保留总售价，会出现完全共线性
    x = scaler.fit_transform(normal_house.loc[:, ("area", "year", "shi", "ting", "layers", "height_state", "中", "低", "高", "东北向",
                                         "东南向", "东向", "东西向", "北向", "南北向", "南向", "西北向", "西南向", "西向", "万家湾", "光华", "八宝街",
                                         "内光华", "内金沙", "外光华", "外金沙", "天府广场", "府南新区", "杜甫草堂", "浣花小区", "石人小区", "苏坡",
                                         "草市街", "西南财大", "贝森", "长顺街", "顺城街", "骡马市")])
    y = normal_house.loc[:, "price_cor"]
    # 划分训练集与测试集；测试集选取全部数据的20%
    train = []
    test = []
    for i in range(normal_house.shape[0]):
        if random.random() > 0.2:
            train.append(i)
        else:
            test.append(i)
    x_test = x[test]
    x_train = x[train]
    y_test = y[test]
    y_train = y[train]

    # 多元线性回归
    linreg = LinearRegression()
    lin_fbs = linreg.fit(x_train, y_train)
    y_lin = lin_fbs.predict(x_test)
    y_hat_2 = lin_fbs.predict(x_train)

    fig = plt.figure(figsize=(16, 16), dpi=150)
    plt.subplots_adjust(wspace=0.1, hspace=0.3)
    x_label = np.arange(1, len(y_test))

    plt.subplot(211)
    plt.plot(x_label, y_test[:-1], linestyle='--', linewidth=2, label='y_test 实际')
    plt.plot(x_label, y_lin[:-1], linestyle='--', linewidth=1, label='y_test 预测')
    plt.title('Prediction\n $Price$')
    plt.legend()

    plt.subplot(212)
    plt.plot(x_label, y_test[:-1] - y_lin[:-1], linestyle='--', linewidth=2, label='y_test 实际')
    plt.title('Prediction\n $e$')
    plt.legend()

    # 回测
    R_square_3 = r2_score(y_train, y_hat_2)
    EVS_3 = explained_variance_score(y_train, y_hat_2)
    MSE_3 = mean_squared_error(y_train, y_hat_2)
    # 预测
    R_square_4 = r2_score(y_test, y_lin)
    EVS_4 = explained_variance_score(y_test, y_lin)
    MSE_4 = mean_squared_error(y_test, y_lin)

    title = ["area", "year", "shi", "ting", "layers", "height_state", "中", "低", "高", "东北向", "东南向", "东向", "东西向", "北向",
             "南北向", "南向", "西北向", "西南向", "西向", "万家湾", "光华", "八宝街", "内光华", "内金沙", "外光华", "外金沙", "天府广场", "府南新区", "杜甫草堂",
             "浣花小区", "石人小区", "苏坡", "草市街", "西南财大", "贝森", "长顺街", "顺城街", "骡马市"]
    coef = lin_fbs.coef_.tolist()
    c = {
        "title": title,
        "coef": coef
    }
    pd.DataFrame(c).sort_values(by="coef", ascending=False).reset_index(drop=True)

    # 支持向量机
    svr_rbf = SVR(kernel='rbf', C=100)
    svr_rbf.fit(x_train, y_train)

    y_svr = svr_rbf.predict(x_test)
    y_hat_1 = svr_rbf.predict(x_train)

    fig = plt.figure(figsize=(16, 16), dpi=150)
    plt.subplots_adjust(wspace=0.1, hspace=0.3)
    x_label = np.arange(1, len(y_test))

    plt.subplot(211)
    plt.plot(x_label, y_test[:-1], linestyle='--', linewidth=2, label='y_test 实际')
    plt.plot(x_label, y_svr[:-1], linestyle='--', linewidth=1, label='y_test 预测')
    plt.title('Prediction\n $Price$')
    plt.legend()

    plt.subplot(212)
    plt.plot(x_label, y_test[:-1] - y_svr[:-1], linestyle='--', linewidth=2, label='y_test 实际')
    plt.title('Prediction\n $e$')
    plt.legend()

    # 回测
    R_square_1 = r2_score(y_train, y_hat_1)
    EVS_1 = explained_variance_score(y_train, y_hat_1)
    MSE_1 = mean_squared_error(y_train, y_hat_1)
    # 预测
    R_square_2 = r2_score(y_test, y_svr)
    EVS_2 = explained_variance_score(y_test, y_svr)
    MSE_2 = mean_squared_error(y_test, y_svr)
