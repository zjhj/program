#!/usr/bin/python3
# -*- coding:utf-8 -*-

import random
import math
import time
import sys

def append_time( func ):
	def wrapper( *args,**kwargs ):
		time1 = time.time()
		back_data = func( *args,**kwargs )
		time2 = time.time()
		return ( time2-time1,back_data )
	return wrapper

@append_time
def selection_sort( need_sort ):
	sort_data = need_sort

	for i in range( len(sort_data)-1 ):
		for j in range( i+1,len(sort_data) ):
			if sort_data[j] < sort_data[i]:
				sort_data[j],sort_data[i] = sort_data[i],sort_data[j]

	return sort_data

@append_time
def bubble_sort( need_sort ):
	sort_data = need_sort

	for i in range( len(sort_data)-1,0,-1 ):
		for j in range(i):
			if sort_data[j] > sort_data[i]:
				sort_data[i],sort_data[j] = sort_data[j],sort_data[i]
	return sort_data

def quick_sort( need_sort ):
	sort_data = need_sort


	if len(need_sort) <= 1:
		return
	curr_data = sort_data[0]

	for i in range( 1,len(sort_data) ):
		if curr_data<i:
	return sort_data

		
@append_time
def insertion_sort( need_sort ):
	sort_data = need_sort

	for i in range( len(sort_data)-1 ):
		curr_data = sort_data[i+1]
		for j in range( i,-1,-1 ):
			if curr_data < sort_data[j]:
				sort_data[j+1] = sort_data[j]
			else:
				break
		sort_data[j+1] = curr_data

	return sort_data

@append_time
def shell_sort( need_sort ):
	sort_data = need_sort

	gap = len(sort_data)
	while True:
		gap = math.floor( gap/2 )

		for i in range( gap ):
			for j in range( i,len(sort_data)-gap,gap ):
				curr_data = sort_data[j+gap]
				for k in range( j,-gap-1,-gap ):
					if curr_data < sort_data[k]:
						sort_data[k+gap] = sort_data[k]
					else:
						break
				sort_data[k+gap] = curr_data

			# print( sort_data,end="\n\n" )

		if gap == 1:
			break

	return sort_data

def do_main():
	try:
		max_number = 20
		if len(sys.argv)>1:
			try:
				max_number = int(sys.argv[1])
			except:
				pass

		need_sort = list()

		for _ in range(max_number):
			need_sort.append( math.floor(random.random()*50*max_number) )
		# print( "Orginal Data:{0}".format(need_sort) )

		# print( insert_sort(need_sort) )
		# print( insertion_sort(need_sort)[0] )
		# print( bubble_sort(need_sort)[0] )
		# print( selection_sort(need_sort)[0] )
		print( shell_sort(need_sort)[0] )
		# print( shell_sort(need_sort) )

	except Exception as ex:
		print( ex )

if __name__ == '__main__':
	do_main()
