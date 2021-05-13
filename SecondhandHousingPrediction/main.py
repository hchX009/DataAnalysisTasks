from get_second_hand_housing_data_in_csv import *
from pretreatment_second_hand_housing_data import *
from predict_second_hand_housing_data import *

if __name__ == '__main__':
    qyq_second_hand_housing_data = read_second_hand_housing_data()
    print("\n得到青羊区二手房清洗后的数据：")
    print(qyq_second_hand_housing_data)
    print("\n预处理青羊区二手房的数据：")
    pretreatment_data = pretreatment_second_hand_data(qyq_second_hand_housing_data)
    print("\n利用预处理青羊区二手房的数据得到数据的测试集和训练集：")
    data_set = get_data_set(pretreatment_data)
    # print(data_set)
    print("使用多元线性回归预测：")
    multiple_linear_regression(data_set)
    print("使用支持向量机预测：")
    support_vector_machine(data_set)
