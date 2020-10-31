#!/usr/bin/python3
#  -*- coding:utf-8 -*-

import pycurl
import traceback

from io import BytesIO

def do_main():
	while True:
		try:
			data_buf = BytesIO()
			head_buf = BytesIO()

			c = pycurl.Curl()

			c.setopt( c.URL,'http://183.207.214.244:8008/#/' )
			c.setopt( c.WRITEDATA, data_buf )
			c.setopt( c.WRITEHEADER, head_buf )
			c.setopt( c.FOLLOWLOCATION,True )
			c.setopt( c.TIMEOUT,1 )
			c.perform()
			c.close()

			print( data_buf.getvalue().decode() )
			print( head_buf.getvalue().decode() )

		except Exception as ex:
			print( ex )
			traceback.print_exc()

if __name__ == '__main__':
	do_main()
