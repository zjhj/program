#!/usr/bin/python3
# -*- coding:utf-8 -*-
from sklearn import datasets
iris = datasets.load_iris()
print( '数据集X：', iris.data.shape )
print( '数据集Y：', iris.target.shape )
