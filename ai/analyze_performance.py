#!/usr/bin/python3
# -*- coding:utf-8 -*-

from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import traceback
import argparse
import json

threshold_min  = 0.01
# threshold_max  = 0.03
# threshold_step = 0.01

def do_analyze( performance_file, target_data ):
	df = pd.read_excel( performance_file,sheet_name=None,header=1 )
	# 逐个sheet处理性能文件
	for curr_sheet in target_data:
		# 逐个处理指定列
		for curr_item in target_data[curr_sheet]:
			curr_df = df[curr_sheet][[curr_item]]
			# curr_df.replace( '--',np.nan )
			curr_df = curr_df.drop( curr_df[curr_df[curr_item]=='--'].index )

			curr_denominator = len( curr_df )
			# 指定簇数范围2-10进行聚类
			for i in range( 2,11 ):
				kmeans = KMeans( n_clusters=i )
				kmeans.fit( curr_df )
				# 追加聚类结果列，并计算占比最小簇所占比例
				curr_df.insert( 1,'cluster',kmeans.labels_ )
				curr_numerator = curr_df.groupby('cluster').count().sort_values(by=curr_item)[:1].values[0][0]
				curr_div = curr_numerator/curr_denominator
				# 在占比小于阈值时退出循环
				if curr_div < threshold_min:
					curr_mean = curr_df.groupby('cluster').count().sort_values(by=curr_item)[:1].index[0]
					print( "Item: {}, n_cluster: {}, abnormal number: {}".format(curr_item,i,curr_numerator) )
					print( curr_df[curr_df['cluster']==curr_mean] )
					break
				curr_df.pop('cluster')

def argument_init():
	# 参数初始化部分
	# -f用于传入json配置文件，默认为：performance.json
	parser = argparse.ArgumentParser( description="show example" )
	parser.add_argument( "-f", "--file", default="performance.json", help="specify the configuration file" )
	return parser.parse_args()

def do_main():
	try:
		args = argument_init()
		config_data = json.load( open(args.file,'r') )

		# 根据参数文件，逐个处理性能文件
		for curr_file in config_data:
			do_analyze( curr_file, config_data[curr_file] )

	except Exception as ex:
		print( ex )
		traceback.print_exc()

if __name__ == '__main__':
	do_main()
