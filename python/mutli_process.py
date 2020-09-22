#!/usr/bin/python3
# -*- coding:utf-8 -*-

from multiprocessing import Pool,Manager

def func(que,i):
	print('sub process running:'+str(i))
	que.put('sub process info:'+str(i))


if __name__ == '__main__':
	process_pool = Pool(4)
	que = Manager().Queue()
	for i in range(4):
		process_pool.apply_async(func,args=(que,i))
	process_pool.close()
	process_pool.join()
	print('sub processes finished')

	for i in range(4):
		print(que.get())
