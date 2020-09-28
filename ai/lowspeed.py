#!/usr/bin/python3
# -*- coding:utf-8 -*-
import xgboost as xgb
import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn import metrics

from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.ensemble import GradientBoostingClassifier

import matplotlib.pyplot as plt

df = pd.read_csv( "lowspeed.csv" )

df1=df[df['LOWSPEED']==0].sample(len(df[df['LOWSPEED']==1]))
df2=df[df['LOWSPEED']==1]
df=pd.concat([df1,df2])

df.drop( ['cgi'],axis=1,inplace=True )
# min_max_scale=MinMaxScaler()
# df=min_max_scale.fit_transform(df)

"""
Kmean = KMeans(n_clusters=3)
# new_col = Kmean.fit_predict( df[['SUC_CALL_RATE','PRB_UTILIZE_RATE','SUC_CALL_RATE_QCI1','mr','upspeed']] )
df['N_SUC_CALL_RATE'] = Kmean.fit_predict( df[['SUC_CALL_RATE']] )
df['N_PRB_UTILIZE_RATE'] = Kmean.fit_predict( df[['PRB_UTILIZE_RATE']] )
df['N_SUC_CALL_RATE_QCI1'] = Kmean.fit_predict( df[['SUC_CALL_RATE_QCI1']] )
df['N_mr'] = Kmean.fit_predict( df[['mr']] )
df['N_upspeed'] = Kmean.fit_predict( df[['upspeed']] )
"""

cols = df.columns

X = df.loc[:, [col for col in cols if col != 'LOWSPEED']]
# X = X.loc[:,['cover_type', 'erabnbrmaxestab1', 'SUC_CALL_RATE', 'PRB_UTILIZE_RATE', 'SUC_CALL_RATE_QCI1', 'mr', 'upspeed' ]]
X = X.loc[:,['SUC_CALL_RATE', 'PRB_UTILIZE_RATE', 'SUC_CALL_RATE_QCI1', 'mr', 'upspeed' ]]
# X = X.loc[:,[ 'N_SUC_CALL_RATE', 'N_PRB_UTILIZE_RATE', 'N_SUC_CALL_RATE_QCI1', 'N_mr', 'N_upspeed' ]]
print( X.info() )

y = df.loc[:, 'LOWSPEED']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

regr = GradientBoostingClassifier()
# regr = xgb.XGBClassifier(max_depth=5, learning_rate=0.05, n_estimators=160, objective='binary:logistic')
regr.fit(X_train, y_train)

Y_pred = regr.predict(X_test)
print( Y_pred )
Y_pred[Y_pred > 0.5]=1
Y_pred[Y_pred <= 0.5]=0

print(accuracy_score(y_test, Y_pred))
print(f1_score(y_test, Y_pred, average='macro'))
fpr, tpr, thresholds = metrics.roc_curve(y_test, Y_pred)
print(metrics.auc(fpr, tpr))

con_mat = metrics.confusion_matrix(y_test,Y_pred)
con_mat_norm = con_mat.astype('float') / con_mat.sum(axis=1)[:, np.newaxis]     # 归一化
con_mat_norm = np.around(con_mat_norm, decimals=2)

# === plot ===
plt.figure(figsize=(8, 8))
sns.heatmap(con_mat_norm, annot=True, cmap='Blues')

plt.ylim(0, 10)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.show()
