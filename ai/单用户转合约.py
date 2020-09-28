#!/usr/bin/env python
# coding: utf-8

# # 案例描述

# 电信单用户是指，电信卡只有打电话、上网等基本功能，按需缴费，固定费用一般较低。
# 电信合约用户是指，电信卡除了打电话、上网等基本功能外还可以绑定高流量包、宽带等，固定费用较高。
# 所以对于一些电话较多，流量使用量大的用户，合约用户更合适，节约费用。

# # 训练和测试数据

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import Normalizer,StandardScaler,MinMaxScaler
from sklearn import metrics

from pylab import mpl 
# window系统乱码解决方案
# mpl.rcParams['font.sans-serif'] = ['SimHei']  #指定默认字体 # 设置matplotlib可以显示汉语
# mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号‘-’显示方块的问题

# Mac系统乱码解决方案
plt.rcParams['font.family'] = ['Arial Unicode MS'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
sns.set_style('whitegrid',{'font.sans-serif':['Arial Unicode MS','Arial']})


# In[2]:


df = pd.read_csv(r'单用户转合约.csv')
print(df.shape)
df.head(5)


# # 整理、准备、探索数据

# In[3]:


# 样本是均衡的
df['是否潜在合约用户'].value_counts().to_dict()


# In[4]:


# 数据没有缺失，'业务类型'字段有英文字符
df.info()


# # 清洗与预处理数据

# In[5]:


# 业务类型2G 3G 4G，转化为one-hot编码
g = pd.get_dummies(df['业务类型'],prefix='业务类型')
df = df.join(g)
# df['业务类型'] = df['业务类型'].map({'2G':0,'3G':1,'4G':2})
df.head(5)


# In[6]:


# 表头
cols = df.columns.values.tolist()


# In[7]:


# 删除不用的列
df.drop('用户标识',axis=1,inplace=True)
df.drop('业务类型',axis=1,inplace=True)

cols.remove('用户标识')
cols.remove('业务类型')

print(df.shape) 

# 新特征sum_1 ‘月均上网时长（分）'* '余额'
sum_1 = df.groupby(['免费流量'])['月均上网时长（分）'].sum() 
sum_1 = dict(sum_1)
cols.append('sum_1')
for key in sum_1.keys():   
    df.loc[df['免费流量'].astype(int)==key,'sum_1'] = sum_1[key]*df['月均上网时长（分）']*df['余额']  
df.head(2)


# In[8]:


# 特征相关性分析
np_normal = StandardScaler().fit_transform(df)
df_normal = pd.DataFrame(np_normal,columns=df.columns)
f, ax = plt.subplots(figsize=(12, 12))
ax = sns.heatmap(df_normal.corr(), cmap='Blues', annot=True)
plt.show()


# In[9]:


# 数据拆分为x y
x = df.loc[:,[col for col in cols if col!='是否潜在合约用户']]
y = df.loc[:,'是否潜在合约用户']
print(x.shape)
print(y.shape)


# In[10]:


# 标准化数据
x_std = StandardScaler().fit_transform(x)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
x_train_std,x_test_std,y_train,y_test = train_test_split(x_std,y,test_size=0.3,random_state=0)
x_train_std


# # 模型训练与预测

# In[11]:


# 模型调优
clf = SVC(kernel='rbf',cache_size=1000,random_state=117) 
param_grid = {'C':np.logspace(-5,5,5),'gamma':np.logspace(-9,2,10)}
grid = GridSearchCV(clf,param_grid=param_grid,scoring='accuracy',n_jobs=-1,cv=5)
grid.fit(x_train_std,y_train)


# In[12]:


# 得到最优参数
print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_)


# In[13]:


# svc = SVC()
svc = SVC(C=100000.0, break_ties=False, cache_size=1000, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma=0.0012915496650148853,
    kernel='rbf', max_iter=-1, probability=False, random_state=117,
    shrinking=True, tol=0.001, verbose=False)
svc.fit(x_train_std,y_train)
# 预测结果
y_pred = svc.predict(x_test_std)


# In[14]:


# 模型评估--准确率
score = metrics.accuracy_score(y_test,y_pred)
print('The accuracy score of the model is: {0}'.format(score))
# 模型评估--混淆矩阵
metrics.confusion_matrix(y_test, y_pred)
