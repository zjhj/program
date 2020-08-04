#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd#科学分析
import os
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

# 数据预处理，填充缺失值以及将特征中含有字符的转换为数值型
df = pd.read_csv( "titanic_train.csv" )
# df.dropna()
cols = df.columns

#预处理
def pretreatment(data):
    # 将年龄这一列的数据缺失值进行填充
    data["Age"].fillna(data["Age"].median(),inplace=True)
    #print(data.describe())  # 打印这一列特征中的特征值都有哪些
    #print(data["Sex"].unique())
    '''
    将性别中的男女设置为0 1 值 
    机器学习不能处理的自字符值转换成能处理的数值
    loc定位到哪一行，将data['Sex'] == 'male'的样本Sex值改为0
    loc定位到哪一行，将data['Sex'] == 'female'的样本Sex值改为1
    '''
    data.loc[data["Sex"] == "male", "Sex"] = 0
    data.loc[data["Sex"] == "female", "Sex"] = 1
    data["Embarked"] = data["Embarked"].fillna("S")  # 将登船地点同样转换成数值
    data.loc[data["Embarked"] == "S", "Embarked"] = 0
    data.loc[data["Embarked"] == "C", "Embarked"] = 1
    data.loc[data["Embarked"] == "Q", "Embarked"] = 2
    #print(data["Embarked"].unique())
    #print(data)
    return data

#通过线性回归进行预测
def dome():

    data = pretreatment(df)
    X = data.loc[:, [col for col in cols if col != 'Survived']]
    X = X.loc[:,['Pclass', 'Sex', 'Age',  'Fare', 'Embarked']]
    print(X.info())
    y = data.loc[:, 'Survived']
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    #scikit-learn的线性回归算法
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)

    # #线性回归函数y = w1x1+w2x2+w3x3+...+wnxn的y
    # print(regr.intercept_)
    # #线性回归函数y = w1x1+w2x2+w3x3+...+wnxn的系数，即w1,w2,w3...wn
    # print(regr.coef_)
    # print('********************************************************')
    # print('训练与测试完美的分割线')
    # print('********************************************************')

    #模型拟合测试集
    Y_pred = regr.predict(X_test)

    #预测值y>0.5设置为1
    # 预测值y<=0.5设置为0
    Y_pred[Y_pred > 0.5]=1
    Y_pred[Y_pred <= 0.5]=0

    tmp = pd.DataFrame(Y_pred == y_test)
    print(tmp)
    tmp = tmp['Survived'].value_counts().to_dict()

    print("测试数据总数量", len(y_test))
    print("正确的数量：", tmp[1])
    print("准确率为：", tmp[1]/len(y_test))

    print('********************************************************')
    print('模型评估指标数据如下')
    print('********************************************************')
    #MSE（Mean squared error）,值为0-1之间，越小越好
    print("MSE: %.2f" % mean_squared_error(y_test, Y_pred))
    #R2（Variance score），值为0-1之间，越大越好
    print('R2: %.2f' % r2_score(y_test, Y_pred))

if __name__ == "__main__":
    dome()
    print("")
