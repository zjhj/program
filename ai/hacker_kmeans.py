#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pandas as pd 
import numpy as np
from sklearn.cluster import KMeans 
from sklearn import metrics

#步骤2∶导数据并删除Location
X= pd.read_csv(r'hack_data.csv')
X.drop(['Location'], axis=1, inplace=True)

#步骤3∶使用Scikit-Learn，假设为2分类。

for i in range(2,10):
	Kmean=KMeans(n_clusters=i)
	y_pred= Kmean.fit_predict(X)
	print("%d分类的分数∶%.2f"%(i,metrics.calinski_harabasz_score(X,y_pred)))
