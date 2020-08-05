#!/usr/bin/python3
# -*- coding:utf-8 -*-
import xgboost as xgb

from sklearn.datasets import load_iris
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
print( iris )

X,y = iris.data, iris.target
X_train,X_test,y_train,y_test = train_test_split( X,y,test_size=0.2,random_state=123321 )

model = xgb.XGBClassifier( max_depth=5,learning_rate=0.1,n_estimators=160,silent=True,objective='multi:softmax' )
model.fit( X_train,y_train )

y_pred = model.predict( X_test )
accuracy = accuracy_score( y_test,y_pred )
print( 'accuracy: %2.f%%' % (accuracy*100) )

plot_importance( model )
plt.show()
