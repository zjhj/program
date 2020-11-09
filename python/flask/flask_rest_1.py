from flask import Flask, request
from flask_restful import Resource, Api

from multiprocessing import Process
from os import path

import paramiko
import random
import hashlib
import json

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
	host_ip = '192.168.247.128'
	host_port = 22
	host_username = 'hj'
	host_password = '123321'
	remote_path = '/home/hj'
	locale_path = '/tmp'

	def check_file_format( self,check_files ):
		for curr_file in check_files:
			try:
				json.dumps( open( path.join(locale_path,curr_file),'r' ).read() )
			except Exception as ex:
				print( "{} 的json校验失败！".format(curr_file) )
				return False
		return True

	def check_file_content( self ):
		# 根据名称索引，看类型、长度，以及是否有数据判断是否正确？好多
		return True

	def check_file( self,check_data ):
		# print( "i am child, data: {}".format(check_data) )
		if 'FileNameList' in check_data:
			p = paramiko.Transport( (self.host_ip,self.host_port) )
			p.connect( username=self.host_username, password=self.host_password )
			s = paramiko.SFTPClient.from_transport( p )
			try:
				remote_files = s.listdir( self.remote_path )
				lack_files = []
				for curr_file in check_Data['FileNameList']:
					if curr_file not in remote_files:
						lack_files.append( curr_file )
				if len(lack_files) > 0:
					print( "缺少文件！" )
					print( lack_file )
				else:
					print( "文件都有！" )

				for curr_file in remote_files:
					s.get( path.join(self.remote_path,curr_file), path.join(self.locale_path,curr_file) )
				if not check_file_format( remote_files ):
					return False
				if not check_file_content( remote_files ):
					return False

			except Excetpion as ex:
				print( ex )
		return True
	
	def gen_token( self ):
		curr_token = hashlib.sha256(random.randint(1,1e10)).hexdigest()


	def get(self, todo_id):
		return {todo_id: todos[todo_id]}

	def put(self, todo_id):
		# todos[todo_id] = request.form['data']
		# return {todo_id: todos[todo_id]}
		# print( request.get_data() )
		print( request.headers )

		if todo_id == "pimCmCallBack":
			p = Process( target=self.check_file, args=(request.get_data(),) )
			p.start()
			return None

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
	app.run(debug=True)
