#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pandas as pd 
import numpy as np
from sklearn.cluster import MiniBatchKMeans 
from sklearn import metrics

#步骤2∶导数据并删除Location
X= pd.read_csv(r'hack_data.csv')
X.drop(['Location'], axis=1, inplace=True)

#步骤3∶使用Scikit-Learn，假设为2分类。
Kmean=MiniBatchKMeans(n_clusters=2)
y_pred= Kmean.fit_predict(X)
print("2分类的分数∶%.2f"%(metrics.calinski_harabasz_score(X,y_pred)))

#步骤4∶使用Scikit-Learn，假设为3分类。
from sklearn.cluster import KMeans 
Kmean=MiniBatchKMeans(n_clusters=3)
y_pred=Kmean.fit_predict(X)
print("3分类的分数∶%.2f"%(metrics.calinski_harabasz_score(X,y_pred)))
