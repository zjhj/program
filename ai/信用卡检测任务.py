#!/usr/bin/env python3
# coding: utf-8

# # 案例描述

# 基于信用卡交易记录数据建立分类模型来预测哪些交易记录是异常的哪些是正常的。

# # 训练和测试数据

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import gzip

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import confusion_matrix,recall_score,classification_report 
from sklearn.model_selection import cross_val_predict

df = pd.read_csv( gzip.open('creditcard.csv.gz') )
df.head()

# # 整理、准备、探索数据

# In[3]:


#样本数据非常不均衡
count_classes = df['Class'].value_counts()
count_classes


# # 清洗与预处理数据

# In[4]:


############下采样数据均衡############
X = df.loc[:, df.columns != 'Class']
y = df.loc[:, df.columns == 'Class']
# 得到所有异常样本的索引
number_records_fraud = len(df[df.Class == 1])
fraud_indices = np.array(df[df.Class == 1].index)

# 得到所有正常样本的索引
normal_indices = df[df.Class == 0].index

# 在正常样本中随机采样出指定个数的样本，并取其索引
random_normal_indices = np.random.choice(normal_indices, number_records_fraud, replace = False)
# random_normal_indices = np.array(random_normal_indices)
# 有了正常和异常样本后把它们的索引都拿到手
under_sample_indices = np.concatenate([fraud_indices,random_normal_indices])
# 根据索引得到下采样所有样本点
under_sample_data = df.loc[under_sample_indices,:]
X_undersample = under_sample_data.loc[:, under_sample_data.columns != 'Class']
y_undersample = under_sample_data.loc[:, under_sample_data.columns == 'Class']

# 下采样 样本比例
print("正常样本所占整体比例: ", len(under_sample_data[under_sample_data.Class == 0])/len(under_sample_data))
print("异常样本所占整体比例: ", len(under_sample_data[under_sample_data.Class == 1])/len(under_sample_data))
print("下采样策略总体样本数量: ", len(under_sample_data))


# In[5]:


#标准化数据
df['normAmount'] = StandardScaler().fit_transform(df['Amount'].values.reshape(-1, 1))
df = df.drop(['Time','Amount'],axis=1)
df.head()


# In[6]:


# 数据拆分为训练集与测试集
X_train_undersample, X_test_undersample, y_train_undersample, y_test_undersample = train_test_split(X_undersample
,y_undersample,test_size = 0.3,random_state = 0)


# In[7]:


############Kfold交叉验证############
def printing_Kfold_scores(x_train_data,y_train_data):
    fold = KFold(5,shuffle=True) 
    # 定义不同力度的正则化惩罚力度
    c_param_range = [0.01]
    # k-fold 表示K折的交叉验证，这里会得到两个索引集合: 训练集 = indices[0], 验证集 = indices[1]
    recall_accs = []
    #一步步分解来执行交叉验证
    for iteration, indices in enumerate(fold.split(x_train_data)):

        # 指定算法模型，并且给定参数
        lr = LogisticRegression(C = c_param_range[0], penalty = 'l2')

        # 训练模型，注意索引不要给错了，训练的时候一定传入的是训练集，所以X和Y的索引都是0
        lr.fit(x_train_data.iloc[indices[0],:],y_train_data.iloc[indices[0],:].values.ravel())

        # 建立好模型后，预测模型结果，这里用的就是验证集，索引为1
        y_pred_undersample = lr.predict(x_train_data.iloc[indices[1],:].values)

        # 有了预测结果之后就可以来进行评估了，这里recall_score需要传入预测值和真实值。
        recall_acc = recall_score(y_train_data.iloc[indices[1],:].values,y_pred_undersample)
        # 一会还要算平均，所以把每一步的结果都先保存起来。
        recall_accs.append(recall_acc)
        print('Iteration ', iteration,': 召回率 = ', recall_acc)
    print('平均召回率 ', np.mean(recall_accs))  
    return c_param_range[0]


# In[8]:


#Recall = TP/(TP+FN)
best_c = printing_Kfold_scores(X_train_undersample,y_train_undersample)
best_c


# # 模型训练与预测

# In[9]:


# 逻辑回归模型
lr = LogisticRegression(C = best_c, penalty = 'l2')
lr.fit(X_train_undersample,y_train_undersample.values.ravel())
y_pred_undersample = lr.predict(X_test_undersample.values)


# # 模型评估与调优

# In[12]:


# 自定义混淆矩阵
def plot_confusion_matrix(cm, classes,title='Confusion matrix',cmap=plt.cm.Blues):
    """绘制混淆矩阵"""
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)
    import itertools 
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


# In[13]:


# 计算所需值
cnf_matrix = confusion_matrix(y_test_undersample,y_pred_undersample)
np.set_printoptions(precision=2)

print("召回率: ", cnf_matrix[1,1]/(cnf_matrix[1,0]+cnf_matrix[1,1]))
print("准确率: ", (cnf_matrix[1,1]+cnf_matrix[0,0])/(cnf_matrix[1,0]+cnf_matrix[1,1]+cnf_matrix[0,0]+cnf_matrix[0,1]))

# 绘图
class_names = [0,1]
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, title='Confusion matrix')
plt.show()


# In[14]:


############阈值对结果的影响############
'''随着阈值的上升, recall值在降低, 也就是判断信用卡欺诈的条件越来越严格.并且阈值取0.5,0.6时相对效果较好'''
# 用之前最好的参数来进行建模
lr = LogisticRegression(C = 0.01, penalty = 'l2')
# 训练模型，还是用下采样的数据集
lr.fit(X_train_undersample,y_train_undersample.values.ravel())
# 得到预测结果的概率值
y_pred_undersample_proba = lr.predict_proba(X_test_undersample.values)
#指定不同的阈值
thresholds = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
plt.figure(figsize=(10,10))
j = 1
# 用混淆矩阵来进行展示
for i in thresholds:
    y_test_predictions_high_recall = y_pred_undersample_proba[:,1] > i

    plt.subplot(3,3,j)
    j += 1
    
    cnf_matrix = confusion_matrix(y_test_undersample,y_test_predictions_high_recall)
    np.set_printoptions(precision=2)

    print("给定阈值为:",i,"时测试集召回率: ", cnf_matrix[1,1]/(cnf_matrix[1,0]+cnf_matrix[1,1]))

    class_names = [0,1]
    plot_confusion_matrix(cnf_matrix, classes=class_names, title='Threshold >= %s'%i) 


# In[ ]:





# In[ ]:




