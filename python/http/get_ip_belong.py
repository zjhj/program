#!/usr/bin/python3
#  -*- coding:utf-8 -*-

import pycurl
import traceback

from io import BytesIO

def do_main():
	try:
		data_buf = BytesIO()
		head_buf = BytesIO()

		c = pycurl.Curl()

		c.setopt( c.URL,'http://ip138.com/ips1388.asp?ip=112.252.21.184&action=2' )
		c.setopt( c.WRITEDATA, data_buf )
		c.setopt( c.WRITEHEADER, head_buf )
		c.setopt( c.FOLLOWLOCATION,True )
		c.perform()
		c.close()

		print( data_buf.getvalue().decode() )
		print( head_buf.getvalue().decode() )

	except Exception as ex:
		print( ex )
		traceback.print_exc()

if __name__ == '__main__':
	do_main()
