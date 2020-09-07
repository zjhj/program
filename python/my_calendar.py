#!/usr/bin/python3
# -*- coding:utf-8 -*-
# input xxxxyy

import datetime

inq_month = input( '输入年月(yyyymm)：' )
# print( inq_month )
print( "" )

title = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

for i in title:
	print( "{:<10s}".format(i), end="" )
print( "" )

curr_day = datetime.date.today()
curr_wday = 1

inq_day_01 = datetime.date( int(inq_month[:4]),int(inq_month[4:]),1 )
offset = ( (inq_day_01-curr_day).days + curr_wday ) % 7

for i in range(offset):
	print( "{:<10s}".format(" "),end="" )

month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
curr_year = int( inq_month[:4] )
curr_mday = 0
if int(inq_month[4:]) == 2 and ( curr_year % 400 == 0 or ( curr_year%100 !=0 and curr_year%4 == 0 ) ):
	curr_mdays = 29
else:
	curr_mdays = month_days[int(inq_month[4:])-1]

# print( "curr_mdays:{},i:{}".format(curr_mdays,i) )
 
for j in range(1,curr_mdays+1):
	print( "  {:<8d}".format(j),end="" )
	# print( j,end=" " )
	offset += 1
	if offset%7 == 0:
		offset = 0
		print( "" )
print( "" )
