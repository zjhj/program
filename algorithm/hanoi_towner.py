#!/usr/bin/python3
# -*- coding:utf-8 -*-

def move( n, a, buffer, c ):
	if n == 1:
		print(a,"->",c)
		return
	move( n-1, a, c, buffer )
	move( 1, a, buffer, c )
	move( n-1, buffer, a, c )

move( 3, "a", "b", "c" )
