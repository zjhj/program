#!/usr/bin/python3
#  -*- coding:utf-8 -*-

class LNode:
	def __init__( self, elem, next_=None ):
		self.elem = elem
		self.next = next_

class LinkedListUnderflow( ValueError ):
	pass

class LList:
	def __init__( self ):
		self._head = None
		self._length = 0
	
	def is_empty( self ):
		return self._head is None

	def prepend( self, elem ):
		self._head = LNode( elem,self._head )
		self._length += 1
	
	def append( self, elem ):
		p = self._head
		while p.next != None:
			p = p.next
		p.next = LNode( elem )
		self._length += 1
	
	def get_length( self ):
		return self._length
	
	def pop( self ):
		if self.is_empty():
			raise LinkedListUnderflow( "in pop" )
		e = self._head.elem
		self._head = self._head.next
		self._length -= 1
		return e

"""
q = LNode(13)
a = LNode( 16,q )
b = LNode( 17,a )
c = LNode( 18,b )

head = c

p = head
while p != None:
	print( p.elem )
	p = p.next
"""

a = LList()
print( a.is_empty(),a.get_length() )

a.prepend( 'a' )
a.prepend( 'b' )
a.prepend( 'c' )
a.append( 'A' )
a.append( 'B' )
a.append( 'c' )


print( a.is_empty(),a.get_length() )

try:
	print( a.pop() )
	print( a.pop() )
	print( a.pop() )
	print( a.pop() )
	print( a.pop() )
	print( a.pop() )
	print( a.pop() )
except Exception as ex:
	print( ex )

print( a.is_empty(),a.get_length() )
