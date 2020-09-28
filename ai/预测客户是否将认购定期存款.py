#!/usr/bin/env python
# coding: utf-8

# # 案例描述
银行机构，通过电话营销给客户，认购定期存款。但这样的营销活动客户转化率特别低。很多客户不需要认购定期存款，且反感这样骚扰型的营销活动。因此需要一个模型对客户进行分类，能精准的告知营销人员，哪些是有这样需求的潜在客户。
分类的目的是预测客户是否将认购定期存款（变量y）。

数据集包含4张表的信息，表字段描述如下：
银行客户资料
age年龄：（数字）
job职位：职位类型（类别：“管理员”，“蓝领”，“企业家”，“女佣”，“管理”，“退休”，“自雇”，“服务”，“学生”，“技术人员”，“待业”，“未知”）
marital婚姻状况：婚姻状况（类别：“离婚”，“已婚”，“单身”，“未知”；注：“离婚”是指离婚或丧偶）
education教育：（类别：“基本4y”，“基本6y”，“基本9y”，“高中”，“文盲”，“专业课程”，“大学学位”，“未知”）
default违约：信用违约吗？（类别：“否”，“是”，“未知”）
housing住房：有住房贷款吗？（类别：“否”，“是”，“未知”）
loan贷款：有个人贷款吗？（类别：“否”，“是”，“未知”）
    
与当前广告的最后联系人相关信息
contact联系人：联系人通讯类型（类别：“手机”，“座机”）
month月：一年中的最后一个接触月（类别：“ jan”，“ feb”，“ mar”，...，“ nov”，“ dec”）
Day_of_week：一周中的最后联系日期（类别：“ mon”，“ tue”，“ wed”，“ thu”，“ fri”）
duration持续时间：最后一次接触持续时间，以秒为单位（数字）。重要说明：此属性对输出目标有很大影响（例如，如果duration = 0，则y ='no'）。然而，在执行呼叫之前，持续时间是未知的。同样，在通话结束后，y显然是已知的。因此，该输入仅应出于基准目的而包括在内，如果要使用一个现实的预测模型，则应将其丢弃。
    
其他属性
campaign广告活动：在此广告活动期间和为此客户执行的联系数量（数字，包括最后一次联系）
Pdays：上一次广告系列中与客户最后一次联系之后经过的天数（数字； 999表示以前未与客户联系）
previous上一个：此广告系列之前和为此客户的联系次数（数字）
poutcome成果：先前营销活动的结果（分类：“失败”，“不存在”，“成功”）

社会和经济背景属性
Emp.var.rate：就业变动率-季度指标（数字）
Cons.price.idx：消费者物价指数-每月指标（数字）
Cons.conf.idx：消费者信心指数-每月指标（数字）
Euribor3m：3个月的euribor费用-每日指标（数字）
nr.employed 雇用人数：雇员人数-季度指标（数字）
# # 训练和测试数据

# In[1]:


# pip install imbalanced-learn


# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler, label_binarize
from sklearn.metrics import accuracy_score,confusion_matrix,roc_curve, auc, f1_score, precision_score, recall_score
from sklearn.svm import SVC
from imblearn.over_sampling import SMOTE, ADASYN
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
# window系统乱码解决方案
# mpl.rcParams['font.sans-serif'] = ['SimHei']  #指定默认字体 # 设置matplotlib可以显示汉语
# mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号‘-’显示方块的问题

# Mac系统乱码解决方案
plt.rcParams['font.family'] = ['Arial Unicode MS'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
sns.set_style('whitegrid',{'font.sans-serif':['Arial Unicode MS','Arial']})


# In[3]:


df = pd.read_csv("/Users/fangyong/work/data/bank-additional-full.csv",sep=';')
header = {'y':'label','age':'年龄','job':'职位','marital':'婚姻状况','education':'教育程度','default':'是否有信用违约',
          'housing':'是否有住房贷款','loan':'是否有个人贷款','contact':'联系人方式','month':'月','day_of_week':'星期',
          'duration':'通话时长','campaign':'广告活动期间和客户联系的次数','pdays':'距离上一次广告活动之后经过的天数',
          'previous':'联系过几次','poutcome':'先前营销活动是否成功',
          'emp.var.rate':'就业变动率','cons.price.idx':'物价指数','cons.conf.idx':'信心指数',
          'euribor3m':'3个月的欧洲费用','nr.employed':'雇用人数'}
df.rename(columns=header,inplace=True)
df.tail()


# # 整理、准备、探索数据

# In[4]:


# 数据没有缺失，总共21列，有11列字段有英文字符，需要进行数据清洗与预处理
df.info()


# In[5]:


#正负样本不均衡
df['label'].value_counts()


# # 探索数据--图形分析--特征与label的相关性

# In[6]:


#正负样本
data1 = df[df['label'] == 'yes']
data2 = df[df['label'] == 'no']


# In[7]:


# 认购定期存款，是否与今天是周一、周二、周三、周四、周五的心情有关。
# 认购定期存款，是否与月份有关。
# 认购定期存款，是否与职业（“管理员”，“蓝领”，“企业家”，“女佣”，“管理”，“退休”，“自雇”，“服务”，“学生”，“技术人员”，“待业”，“未知”）有关。
# 认购定期存款，是否与教育程度（“基本4y”，“基本6y”，“基本9y”，“高中”，“文盲”，“专业课程”，“大学学位”，“未知”）有关。
fig, ax = plt.subplots(2, 2, figsize=(12,10))

b1 = ax[0, 0].bar(data1['星期'].unique(),height = data1['星期'].value_counts(),color='#000000')
b2 = ax[0, 0].bar(data2['星期'].unique(),height = data2['星期'].value_counts(),bottom = data1['星期'].value_counts(),color = '#DC4405') 
ax[0, 0].title.set_text('周1-周5分布统计')

#ax[0, 0].legend((b1[0], b2[0]), ('Yes', 'No'))
ax[0, 1].bar(data1['月'].unique(),height = data1['月'].value_counts(),color='#000000')
ax[0, 1].bar(data2['月'].unique(),height = data2['月'].value_counts(),bottom = data1['月'].value_counts(),color = '#DC4405') 
ax[0, 1].title.set_text('月分布统计')

ax[1, 0].bar(data1['职位'].unique(),height = data1['职位'].value_counts(),color='#000000')
ax[1, 0].bar(data1['职位'].unique(),height = data2['职位'].value_counts()[data1['职位'].value_counts().index],bottom = data1['职位'].value_counts(),color = '#DC4405') 
ax[1, 0].title.set_text('职业分布统计')

ax[1, 0].tick_params(axis='x',rotation=90)
ax[1, 1].bar(data1['教育程度'].unique(),height = data1['教育程度'].value_counts(),color='#000000') #row=0, col=1
ax[1, 1].bar(data1['教育程度'].unique(),height = data2['教育程度'].value_counts()[data1['教育程度'].value_counts().index],bottom = data1['教育程度'].value_counts(),color = '#DC4405') 
ax[1, 1].title.set_text('教育程度分布统计')

ax[1, 1].tick_params(axis='x',rotation=90)
#ax[0, 1].xticks(rotation=90)
plt.figlegend((b1[0], b2[0]), ('Yes', 'No'),loc="right",title = "认购定期存款")
plt.show()


# In[8]:


# 认购定期存款，是否与婚姻状况有关。
# 认购定期存款，是否与有住房贷款有关。
# 认购定期存款，是否与有个人贷款有关。
# 认购定期存款，是否与联系人方式不同有关。
# 认购定期存款，是否与有信用违约有关。
# 认购定期存款，是否与先前营销活动成功或失败有关。
fig, ax = plt.subplots(2, 3, figsize=(15,10))

b1 = ax[0, 0].bar(data1['婚姻状况'].unique(),height = data1['婚姻状况'].value_counts(),color='#000000')
b2 = ax[0, 0].bar(data1['婚姻状况'].unique(),height = data2['婚姻状况'].value_counts()[data1['婚姻状况'].value_counts().index],bottom = data1['婚姻状况'].value_counts(),color = '#DC4405') 
ax[0, 0].title.set_text('婚姻状况')

#ax[0, 0].legend((b1[0], b2[0]), ('Yes', 'No'))
ax[0, 1].bar(data1['是否有住房贷款'].unique(),height = data1['是否有住房贷款'].value_counts(),color='#000000')
ax[0, 1].bar(data1['是否有住房贷款'].unique(),height = data2['是否有住房贷款'].value_counts()[data1['是否有住房贷款'].value_counts().index],bottom = data1['是否有住房贷款'].value_counts(),color = '#DC4405') 
ax[0, 1].title.set_text('是否有住房贷款')

ax[0, 2].bar(data1['是否有个人贷款'].unique(),height = data1['是否有个人贷款'].value_counts(),color='#000000')
ax[0, 2].bar(data1['是否有个人贷款'].unique(),height = data2['是否有个人贷款'].value_counts()[data1['是否有个人贷款'].value_counts().index],bottom = data1['是否有个人贷款'].value_counts(),color = '#DC4405') 
ax[0, 2].title.set_text('是否有个人贷款')

ax[1, 0].bar(data1['联系人方式'].unique(),height = data1['联系人方式'].value_counts(),color='#000000')
ax[1, 0].bar(data1['联系人方式'].unique(),height = data2['联系人方式'].value_counts()[data1['联系人方式'].value_counts().index],bottom = data1['联系人方式'].value_counts(),color = '#DC4405') 
ax[1, 0].title.set_text('联系人方式')

ax[1, 1].bar(data1['是否有信用违约'].unique(),height = data1['是否有信用违约'].value_counts(),color='#000000')
ax[1, 1].bar(data1['是否有信用违约'].unique(),height = data2['是否有信用违约'].value_counts()[data1['是否有信用违约'].value_counts().index],bottom = data1['是否有信用违约'].value_counts(),color = '#DC4405') 
ax[1, 1].title.set_text('是否有信用违约')

ax[1, 2].bar(data1['先前营销活动是否成功'].unique(),height = data1['先前营销活动是否成功'].value_counts(),color='#000000')
ax[1, 2].bar(data1['先前营销活动是否成功'].unique(),height = data2['先前营销活动是否成功'].value_counts()[data1['先前营销活动是否成功'].value_counts().index],bottom = data1['先前营销活动是否成功'].value_counts(),color = '#DC4405') 
ax[1, 2].title.set_text('先前营销活动是否成功')

plt.figlegend((b1[0], b2[0]), ('Yes', 'No'),loc="right",title = "认购定期存款")
plt.show()


# In[9]:


# 认购定期存款，是否与年龄有关。
# 认购定期存款，是否与通话时长有关。
# 认购定期存款，是否与广告活动期间和客户联系的次数有关。
# 认购定期存款，是否与距离上一次广告活动之后的天数长短有关。
fig, ax = plt.subplots(2, 2, figsize=(12,10))

ax[0, 0].hist(data2['年龄'],color = '#DC4405',alpha=0.7,bins=20, edgecolor='white') 
ax[0, 0].hist(data1['年龄'],color='#000000',alpha=0.5,bins=20, edgecolor='white')
ax[0, 0].title.set_text('年龄')

ax[0, 1].hist(data2['通话时长'],color = '#DC4405',alpha=0.7, edgecolor='white') 
ax[0, 1].hist(data1['通话时长'],color='#000000',alpha=0.5, edgecolor='white')
ax[0, 1].title.set_text('通话时长')

ax[1, 0].hist(data2['广告活动期间和客户联系的次数'],color = '#DC4405',alpha=0.7, edgecolor='white') 
ax[1, 0].hist(data1['广告活动期间和客户联系的次数'],color='#000000',alpha=0.5, edgecolor='white')
ax[1, 0].title.set_text('广告活动期间和客户联系的次数')

ax[1, 1].hist(data2[data2['距离上一次广告活动之后经过的天数'] != 999]['距离上一次广告活动之后经过的天数'],color = '#DC4405',alpha=0.7, edgecolor='white') 
ax[1, 1].hist(data1[data1['距离上一次广告活动之后经过的天数'] != 999]['距离上一次广告活动之后经过的天数'],color='#000000',alpha=0.5, edgecolor='white')
ax[1, 1].title.set_text('距离上一次广告活动之后经过的天数')

plt.figlegend((b1[0], b2[0]), ('Yes', 'No'),loc="right",title = "认购定期存款")
plt.show()


# In[10]:


# 认购定期存款，是否与联系客户次数有关。
# 认购定期存款，是否与就业率（季度指标）有关。
# 认购定期存款，是否与消费者物价指数（每月指标）有关。
# 认购定期存款，是否与消费者信心指数（每月指标）有关。
# 认购定期存款，是否与3个月的euribor费用（每日指标）有关。
# 认购定期存款，是否与雇员人数（季度指标）有关。
fig, ax = plt.subplots(2, 3, figsize=(15,10))
ax[0, 0].hist(data2['联系过几次'],color = '#DC4405',alpha=0.7, edgecolor='white') 
ax[0, 0].hist(data1['联系过几次'],color='#000000',alpha=0.5, edgecolor='white')
ax[0, 0].title.set_text('联系过几次')

ax[0, 1].hist(data2['就业变动率'],color = '#DC4405',alpha=0.7, edgecolor='white') 
ax[0, 1].hist(data1['就业变动率'],color='#000000',alpha=0.5, edgecolor='white')
ax[0, 1].title.set_text('就业变动率-季度指标')

ax[0, 2].hist(data2['物价指数'],color = '#DC4405',alpha=0.7, edgecolor='white') 
ax[0, 2].hist(data1['物价指数'],color='#000000',alpha=0.5, edgecolor='white')
ax[0, 2].title.set_text('消费者物价指数-每月指标')

ax[1, 0].hist(data2['信心指数'],color = '#DC4405',alpha=0.7, edgecolor='white') 
ax[1, 0].hist(data1['信心指数'],color='#000000',alpha=0.5, edgecolor='white')
ax[1, 0].title.set_text('消费者信心指数-每月指标')

ax[1, 1].hist(data2['3个月的欧洲费用'],color = '#DC4405',alpha=0.7, edgecolor='white') 
ax[1, 1].hist(data1['3个月的欧洲费用'],color='#000000',alpha=0.5, edgecolor='white')
ax[1, 1].title.set_text('3个月的euribor费用-每日指标')

ax[1, 2].hist(data2['雇用人数'],color = '#DC4405',alpha=0.7, edgecolor='white') 
ax[1, 2].hist(data1['雇用人数'],color='#000000',alpha=0.5, edgecolor='white')
ax[1, 2].title.set_text('雇员人数-季度指标')

plt.figlegend((b1[0], b2[0]), ('Yes', 'No'),loc="right",title = "认购定期存款")
plt.show()


# # 清洗与预处理数据

# In[11]:


predictors = df.iloc[:,0:20]
predictors = predictors.drop(['距离上一次广告活动之后经过的天数'],axis=1)
y = df.iloc[:,20]
X = pd.get_dummies(predictors)


# In[12]:


# 不平衡数据集解决方案--随机欠采样（下采样），从多数类样本中随机选择少量样本，再合并原有少数类样本作为新的训练数据集。
rus = RandomUnderSampler(random_state=0)
X_Usampled, y_Usampled = rus.fit_resample(X, y)
pd.Series(y_Usampled).value_counts()


# In[13]:


# 不平衡数据集解决方案--随机过采样（上采样），从少数类的样本中进行随机采样来增加新的样本。
ros = RandomOverSampler(random_state=0)
X_Osampled, y_Osampled = ros.fit_resample(X, y)
pd.Series(y_Osampled).value_counts()


# SMOTE（Synthetic Minority Oversampling Technique），合成少数类过采样技术．它是基于随机过采样算法的一种改进方案，由于随机过采样采取简单复制样本的策略来增加少数类样本，这样容易产生模型过拟合的问题，即使得模型学习到的信息过于特别(Specific)而不够泛化(General)，SMOTE算法的基本思想是对少数类样本进行分析并根据少数类样本人工合成新样本添加到数据集中.

# In[14]:


# 不平衡数据集解决方案--SMOTE
sm = SMOTE(random_state=0)
X_SMOTE, y_SMOTE = sm.fit_resample(X, y)
pd.Series(y_SMOTE).value_counts()


# # 模型训练与预测

# 使用Perceptron()方法，验证不平衡数据集解决方案，那个更好。很明显SMOTE方案最佳。

# In[15]:


X_train, X_test, y_train, y_test = train_test_split(X_Usampled, y_Usampled, test_size=0.3)
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
perp_model = lm.Perceptron().fit(X_train_std,y_train)
y_pred = perp_model.predict(X_test_std)
print("Accuracy: ",round(accuracy_score(y_test, y_pred),2))


# In[16]:


X_train, X_test, y_train, y_test = train_test_split(X_Osampled, y_Osampled, test_size=0.3)
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
perp_model = lm.Perceptron().fit(X_train_std,y_train)
y_pred = perp_model.predict(X_test_std)
print("Accuracy: ",round(accuracy_score(y_test, y_pred),2))


# In[17]:


X_train, X_test, y_train, y_test = train_test_split(X_SMOTE, y_SMOTE, test_size=0.3)
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
perp_model = lm.Perceptron().fit(X_train_std,y_train)
y_pred = perp_model.predict(X_test_std)
print("Accuracy: ",round(accuracy_score(y_test, y_pred),2))


# In[18]:


mat = confusion_matrix(y_test,y_pred,labels=['no','yes'])
print(mat)
y_test = label_binarize(y_test,classes=['no','yes'])
y_pred = label_binarize(y_pred,classes=['no','yes'])
print("Precision: ",round(precision_score(y_test,y_pred),2),"Recall: ",round(recall_score(y_test,y_pred),2))


# In[19]:


# 数据拆分为训练集与测试集，比例为0.7:0.3
X_train, X_test, y_train, y_test = train_test_split(X_SMOTE, y_SMOTE, test_size=0.3)
# 数据标准化
sc = StandardScaler()
sc.fit(X_train)
sc.fit(X_test)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)


# In[20]:


# 决策树算法模型
tree = DecisionTreeClassifier()
model = tree.fit(X_train_std,y_train)
y_pred = model.predict(X_test_std)
y_test = label_binarize(y_test,classes=['no','yes'])
y_pred = label_binarize(y_pred,classes=['no','yes'])
print("Precision: ",round(precision_score(y_test,y_pred),2),"Recall: ",round(recall_score(y_test,y_pred),2))


# In[21]:


# 随机森林算法模型
forest = RandomForestClassifier()
model = forest.fit(X_train_std,y_train)
y_pred = model.predict(X_test_std)
pd.Series(y_pred).value_counts()
y_test = label_binarize(y_test,classes=['no','yes'])
y_pred = label_binarize(y_pred,classes=['no','yes'])
print("Precision: ",round(precision_score(y_test,y_pred),2),"Recall: ",round(recall_score(y_test,y_pred),2))


# In[22]:


# 逻辑回归算法模型
lr = LogisticRegression(max_iter=10000)
model = lr.fit(X_train_std,y_train)
y_pred = model.predict(X_test_std)
pd.Series(y_pred).value_counts()
y_test = label_binarize(y_test,classes=['no','yes'])
y_pred = label_binarize(y_pred,classes=['no','yes'])
print("Precision: ",round(precision_score(y_test,y_pred),2),"Recall: ",round(recall_score(y_test,y_pred),2))


# In[ ]:


# svm算法模型，线性核函数kernel='linear'
svm = SVC(kernel='linear')
model = svm.fit(X_train_std, y_train)
y_pred = model.predict(X_test_std)
y_test = label_binarize(y_test,classes=['no','yes'])
y_pred = label_binarize(y_pred,classes=['no','yes'])
print("Linear kernel- ","Precision: ",round(precision_score(y_test,y_pred),2),"Recall: ",round(recall_score(y_test,y_pred),2))
fpr_linear, tpr_linear, _ = roc_curve(y_test, y_pred)
roc_auc_linear = auc(fpr_linear, tpr_linear)


# In[ ]:


# svm算法模型，多项式核函数kernel='poly'
svm = SVC(kernel='poly')
model = svm.fit(X_train_std, y_train)
y_pred = model.predict(X_test_std)
y_test = label_binarize(y_test,classes=['no','yes'])
y_pred = label_binarize(y_pred,classes=['no','yes'])
print("poly kernel- ","Precision: ",round(precision_score(y_test,y_pred),2),"Recall: ",round(recall_score(y_test,y_pred),2))
fpr_poly, tpr_poly, _ = roc_curve(y_test, y_pred)
roc_auc_poly = auc(fpr_poly, tpr_poly)


# In[ ]:


# svm算法模型，sigmod核函数kernel='sigmod'
svm = SVC(kernel='sigmoid')
model = svm.fit(X_train_std, y_train)
y_pred = model.predict(X_test_std)
y_test = label_binarize(y_test,classes=['no','yes'])
y_pred = label_binarize(y_pred,classes=['no','yes'])
print("sigmoid kernel- ","Precision: ",round(precision_score(y_test,y_pred),2),"Recall: ",round(recall_score(y_test,y_pred),2))
fpr_sigmoid, tpr_sigmoid, _ = roc_curve(y_test, y_pred)
roc_auc_sigmoid = auc(fpr_sigmoid, tpr_sigmoid)


# In[ ]:


# svm算法模型，径向基核函数kernel='rbf'
svm = SVC(kernel='rbf')
model = svm.fit(X_train_std, y_train)
y_pred = model.predict(X_test_std)
y_test = label_binarize(y_test,classes=['no','yes'])
y_pred = label_binarize(y_pred,classes=['no','yes'])
print("Guassian kernel- ","Precision: ",round(precision_score(y_test,y_pred),2),"Recall: ",round(recall_score(y_test,y_pred),2))
fpr_rbf, tpr_rbf, _ = roc_curve(y_test, y_pred)
roc_auc_rbf = auc(fpr_rbf, tpr_rbf)


# In[ ]:


plt.figure()
lw = 2

plt.plot(fpr_linear, tpr_linear,
         label='Linear Kernel ROC curve (area = {0:0.4f})'
               ''.format(roc_auc_linear),
         color='darkred', linestyle='--', linewidth=2)

plt.plot(fpr_rbf, tpr_rbf,
         label='Gaussian Kernel ROC curve (area = {0:0.4f})'
               ''.format(roc_auc_rbf),
         color='darkgreen', linestyle='--', linewidth=2)

plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.00])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()


# # 5. Conclusion

# 对于给定的数据，探索了数据的可视化，处理数据不平衡的方法以及确定定期存款订阅的最佳预测模型。
# 从可视化中可以得出，在上一次致电的20天内向客户重复广告系列致电会增加订阅。
# 使用SMOTE处理数据不平衡之后，具有高斯内核的SVM在精度和查全率方面表现最佳。

# In[ ]:




