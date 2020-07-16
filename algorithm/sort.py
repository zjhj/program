#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import gzip
import re

is_debug = True

def sort_bubble( data ):
	if is_debug:
		print( "start bubble sort..." )

	sorted_data = data
	data_len = len( sorted_data )

	cnt = 0
	for i in range( data_len ):
		for j in range( data_len-i-1 ):
			if sorted_data[j] > sorted_data[j+1]:
				sorted_data[j],sorted_data[j+1] = sorted_data[j+1],sorted_data[j]
		if is_debug:
			print( sorted_data )
		cnt += 1

	return sorted_data

def sort_selection( data ):
	if is_debug:
		print( "start selection sort..." )

	sorted_data = data.copy()
	data_len = len( sorted_data )

	for i in range( data_len ):
		curr_loc = i
		for j in range( i+1,data_len ):
			if sorted_data[curr_loc] > sorted_data[j]:
				curr_loc = j
		if curr_loc != i:
			sorted_data[curr_loc],sorted_data[i] = sorted_data[i],sorted_data[curr_loc]
		if is_debug:
			print( sorted_data )
			
	return sorted_data

def sort_insertion( data ):
	if is_debug:
		print( "start insertion sort..." )

	sorted_data = data.copy()
	curr_length = 0

	for i in range( 1,len(sorted_data) ):
		if is_debug:
			print( sorted_data )
		curr_length += 1
		for j in range( curr_length ):
			if sorted_data[j] > sorted_data[i]:
				sorted_data.insert( j,sorted_data[i] )
				sorted_data.pop( i+1 )
				break

	"""
	sorted_data = [data[0]]
	curr_length = 0

	for i in range( 1,len(data) ):
		curr_length += 1
		for j in range( curr_length ):
			if sorted_data[j] > data[i]:
				sorted_data.insert( j,data[i] )
				break
			elif j == curr_length-1:
				sorted_data.append( data[i] )
	"""

	return sorted_data

for i in range( 1,len(sys.argv) ):
	curr_f = gzip.GzipFile( sys.argv[i] )

	need_sort = [int(x) for x in re.findall( '[-0-9]+',curr_f.read().decode() )]
	if is_debug:
		print( "Original data:\n{}".format(need_sort) )

	print( sort_insertion(need_sort) )
	print( sort_selection(need_sort) )
	print( sort_bubble(need_sort) )
