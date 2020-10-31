#!/usr/bin/python3
# -*- coding:utf-8 -*-

# from io import StringIO
# from urllib.parse import urlencode
from StringIO import StringIO
from urllib import urlencode

#设置post请求， 上传文件的字段名 上传的文件
#post_file = "/home/ubuntu/avatar.jpg"
# c.setopt(c.HTTPPOST, [("textname", (c.FORM_FILE, post_file))])

import pycurl
import traceback

def do_main():
	try:
		head_buf = StringIO()
		data_buf = StringIO()

		http_head = [ 'Host:10.40.115.200', \
					  'Origin:http://10.40.115.200', \
					  'Cookie:upms-server-session-id=844ebb76-4382-49e6-a744-d3498c9e80f8']

		post_data = { 'startDate':'', 'status':'0', 'endDate':'', 'sort':'desc', 'sort_key':'create_time',
					  'pageIndex':'1', 'pageSize':'10' }

		c = pycurl.Curl()
		c.setopt( c.URL,'http://10.40.115.200/ssa/blockPlatform/getList.do' )
		c.setopt( c.HEADERFUNCTION, head_buf.write )
		c.setopt( c.WRITEFUNCTION, data_buf.write )
		c.setopt( c.POSTFIELDS, urlencode(post_data) )

		c.perform()
		print( data_buf.getvalue() )
		c.close()

	except Exception as ex:
		print( ex )
		traceback.print_exc()

if __name__ == '__main__':
	do_main()
