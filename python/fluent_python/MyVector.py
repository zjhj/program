#!/usr/bin/python3
# -*- coding:utf-8 -*-

from math import hypot

class MyVector:
	def __init__( self, x=0, y=0 ):
		self.x = x
		self.y = y
	
	def __abs__( self ):
		return hypot( self.x, self.y )

	def __repr__( self ):
		return "Vector( {},{} )".format(self.x,self.y)

	def __bool__( self ):
		return bool( abs(self) )

	def __add__( self, other ):
		self.x += other.x
		self.y += other.y

	def __mul__( self, scalar ):
		return MyVector( self.x*scalar, self.y*scalar )
