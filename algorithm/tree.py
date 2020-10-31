#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Tree(object):
	def __init__(self,data,lchild=None,rchild=None):
		self.data = data
		self.lchild = lchild
		self.rchild = rchild

class solution( object ):
	# 已知先序、中序，求后序
	def combin_pro(self,prolist,inlist):
		if not prolist or not inlist:
			return
		root = Tree(prolist[0])
		index = inlist.index(root.data)
		root.lchild = self.combin_pro(prolist[1:index+1],inlist[0:index])
		root.rchild = self.combin_pro(prolist[index+1:],inlist[index+1:])
		return root

	# 已知中序、后序，求先序
	def combin_post(self,inlist,postlist):
		if not inlist or not postlist:
			return
		root = Tree(postlist[-1])
		index = inlist.index(root.data)
		root.lchild = self.combin_post(inlist[0:index],postlist[0:index])
		root.rchild = self.combin_post(inlist[index+1:],postlist[index:len(postlist)-1])

	def print_post( self,root,res=[] ):
		if root == None:
			return
		self.print_post( root.lchild,res )
		self.print_post( root.rchild,res )
		res.append( root.data )
		return res

	def print_mid( self,root,res=[] ):
		if root == None:
			return
		self.print_mid( root.lchild,res )
		res.append( root.data )
		self.print_mid( root.rchild,res )
		return res

	def print_pro( self,root,res=[] ):
		if root == None:
			return
		res.append( root.data )
		self.print_pro( root.lchild,res )
		self.print_pro( root.rchild,res )
		return res

if __name__ == '__main__':
	pro = [0,1,3,7,8,4,9,2,5,6]
	mid = [7,3,8,1,9,4,0,5,2,6]
	post= [7,8,3,9,4,1,5,6,2,0]
	A = solution()

	r = A.combin_pro( pro,mid )
	print( A.print_post( r ) )
	print( A.print_mid( r ) )
	print( A.print_pro( r ) )
