#!/usr/bin/python3
#  -*- coding:utf-8 -*-

import random
import math

class BTree:
	_LEFT  = 1
	_RIGHT = 2

	pre_data  = list()
	in_data   = list()
	post_data = list()
	ts_data   = list()

	def __init__( self ):
		self.root  = None
		self.left  = None
		self.right = None
	
	def append( self,elem,parent=None,side=None ):
		curr_node = BTreeNode( elem )

		if self.root is None:
			self.root = curr_node
		elif parent is not None:
			pass
		else:
			q = [ self.root ]
			while True:
				pop_node = q.pop( 0 )
				if pop_node.left is None:
					pop_node.left  = curr_node
					return
				elif pop_node.right is None:
					pop_node.right = curr_node
					return
				else:
					q.append( pop_node.left )
					q.append( pop_node.right )
	
	def preorder( self, root ):
		if root is None:
			return

		self.pre_data.append( root.elem )
		self.preorder( root.left )
		self.preorder( root.right )
	
	def inorder( self, root ):
		if root is None:
			return

		self.inorder( root.left )
		self.in_data.append( root.elem )
		self.inorder( root.right )
	
	def postorder( self, root ):
		if root is None:
			return

		self.postorder( root.left )
		self.postorder( root.right )
		self.post_data.append( root.elem )

	def transverse( self, root ):
		if root is None:
			return

		p = [root]

		while len(p) > 0:
			pop_node = p.pop( 0 )
			self.ts_data.append( pop_node.elem )
			if pop_node.left is not None:
				p.append( pop_node.left )
			if pop_node.right is not None:
				p.append( pop_node.right )



class BTreeNode:
	def __init__( self,elem,left_=None,right_=None ):
		self.elem = elem
		self.left = left_
		self.right = right_

"""
tree_data = list()
for _ in range(20):
	curr_data = math.floor( random.random()*100 )
	if curr_data not in tree_data:
		tree_data.append( curr_data )
print( "Number: {0}, Data:{1}".format(len(tree_data),tree_data) )

a = BTree()
for _ in tree_data:
	a.append( _ )

a.preorder( a.root )
print( "PreOrder: {0}".format(a.pre_data) )
a.inorder( a.root )
print( "InOrder: {0}".format(a.in_data) )
a.postorder( a.root )
print( "PostOrder: {0}".format(a.post_data) )
a.transverse( a.root )
print( "TransverseOrder:" )
"""


# construct the tree from inorder and preorder
# p_data = a.pre_data

p_data = [38, 86, 12, 3, 55, 5, 39, 49, 68, 19, 30, 97, 87, 40, 42, 14, 26, 72]
# p_data = [3, 20, 21, 8, 72, 25, 29, 9, 79, 24, 82, 38, 94, 90, 6, 71, 68, 89, 87]
i_data = [55, 3, 5, 12, 49, 39, 86, 19, 68, 30, 38, 40, 87, 42, 97, 26, 14, 72]
# i_data = [72, 8, 25, 21, 9, 29, 79, 20, 82, 24, 38, 3, 6, 90, 71, 94, 89, 68, 87]

def construct_tree( data ):
	if len(data) == 0:
		return None
	root = p_data.pop(0)
	curr_pos = data.index( root )
	if curr_pos == 0:
		return BTreeNode( data[curr_pos] )

	return BTreeNode( root,construct_tree(data[:curr_pos]),construct_tree(data[curr_pos+1:]) )

c_root = construct_tree( i_data )

if c_root is None:
	print( "Bad!" )

p = [c_root]
tmp_data = list()
while len(p) > 0:
	pop_node = p.pop( 0 )
	tmp_data.append( pop_node.elem )
	if pop_node.left is not None:
		p.append( pop_node.left )
	if pop_node.right is not None:
		p.append( pop_node.right )

print( tmp_data )

"""
a = BTreeNode( 10 )
b = BTreeNode( 12 )
c = BTreeNode( 9,a,b )

d = BTreeNode( 0 )
e = BTreeNode( 1 )
f = BTreeNode( 2,d,e )

root = BTreeNode( 100,c,f )

print( root.elem, root.left.elem, root.right.elem )
"""
