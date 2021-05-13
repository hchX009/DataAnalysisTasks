# 预测二手房价格数据
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import *
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.family"] = "SimHei"  # 使用支持的黑体中文字体
mpl.rcParams["axes.unicode_minus"] = False  #  用来正常显示负号"-"

plt.rcParams['font.sans-serif'] = ['SimHei']  #  用来正常显示中文标签


# 多元线性回归
def multiple_linear_regression(data_set):
    x_train = data_set["x_train"]
    y_train = data_set["y_train"]
    x_test = data_set["x_test"]
    y_test = data_set["y_test"]

    line_reg = LinearRegression()

    # fit传入数据以及标签即可训练模型
    line_reg_model = line_reg.fit(x_train, y_train)

    # predict用于对数据的预测，它接受输入，并输出预测标签，输出的格式为numpy数组。我们通常使用这个方法返回测试的结果，再将这个结果用于评估模型。
    y_test_predict = line_reg_model.predict(x_test)
    y_train_predict = line_reg_model.predict(x_train)

    # 得到多元线性回归回归系数列表
    # line_reg_model.coef_.tolist()

    # 设置图像显示
    plt.figure(figsize=(16, 16), dpi=150)
    plt.subplots_adjust(wspace=0.1, hspace=0.3)
    x_label = np.arange(1, len(y_test))
    plt.subplot(211)
    plt.plot(x_label, y_test[:-1], linestyle='--', linewidth=2, label='y_test 实际')
    plt.plot(x_label, y_test_predict[:-1], linestyle='--', linewidth=1, label='y_test 预测')
    plt.title('Prediction\n $Price$')
    plt.legend()
    plt.subplot(212)
    plt.plot(x_label, y_test[:-1] - y_test_predict[:-1], linestyle='--', linewidth=2, label='y_test 残差')
    plt.title('Prediction\n $e$')
    plt.legend()
    plt.savefig("./青羊区二手房多元线性回归价格预测.png")
    plt.show()

    # 进行回测和预测
    backtesting_and_predict(y_test, y_train, y_test_predict, y_train_predict)


# 支持向量机
def support_vector_machine(data_set):
    x_train = data_set["x_train"]
    y_train = data_set["y_train"]
    x_test = data_set["x_test"]
    y_test = data_set["y_test"]

    # 支持向量机回归SVR,惩罚参数为100
    # fit传入数据以及标签即可训练模型
    svr_modle = SVR(kernel='rbf', C=100)
    svr_modle.fit(x_train, y_train)

    y_test_svr_predict = svr_modle.predict(x_test)
    y_train_svr_predict = svr_modle.predict(x_train)

    # 设置图像显示
    plt.figure(figsize=(16, 16), dpi=150)
    plt.subplots_adjust(wspace=0.1, hspace=0.3)
    x_label = np.arange(1, len(y_test))
    plt.subplot(211)
    plt.plot(x_label, y_test[:-1], linestyle='--', linewidth=2, label='y_test 实际')
    plt.plot(x_label, y_test_svr_predict[:-1], linestyle='--', linewidth=1, label='y_test 预测')
    plt.title('Prediction\n $Price$')
    plt.legend()
    plt.subplot(212)
    plt.plot(x_label, y_test[:-1] - y_test_svr_predict[:-1], linestyle='--', linewidth=2, label='y_test 残差')
    plt.title('Prediction\n $e$')
    plt.legend()
    plt.savefig("./青羊区二手房支持向量机价格预测.png")
    plt.show()

    # 进行回测和预测
    backtesting_and_predict(y_test, y_train, y_test_svr_predict, y_train_svr_predict)


# 回测和预测
def backtesting_and_predict(y_test, y_train, y_test_predict, y_train_predict):

    # 回测
    R_square_3 = r2_score(y_train, y_train_predict)
    EVS_3 = explained_variance_score(y_train, y_train_predict)
    MSE_3 = mean_squared_error(y_train, y_train_predict)

    # 预测
    R_square_4 = r2_score(y_test, y_test_predict)
    EVS_4 = explained_variance_score(y_test, y_test_predict)
    MSE_4 = mean_squared_error(y_test, y_test_predict)


