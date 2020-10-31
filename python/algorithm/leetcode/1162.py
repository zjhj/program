#!/usr/bin/python3
# -*- coding:utf-8 -*-

import random
import math

class Solution( object ):
	def __init__( self,grid ):
		self.grid = grid
	
	def isValid( self ):
		if type( self.grid ) != list or type( self.grid[0] ) != list:
			return False

		curr_data = self.grid[0][0]

		for i in self.grid:
			for j in i:
				if j != curr_data:
					return True

		return False

	def maxDistance( self ):
		if not self.isValid():
			return -1

		distData = dict()

		for i,line_data in enumerate(self.grid):
			for j,cell_data in enumerate(line_data):
				currDist = -1
				if cell_data == 0:
					isFind = False
					for a in range( 1,len(self.grid)*2-1 ):
						for b in range(0,a+1):
							if ( i-b>=0 and j-a+b>=0 and self.grid[i-b][j-a+b] == 1 ) or \
							   ( i-b>=0 and j+a-b<len(self.grid) and self.grid[i-b][j+a-b] == 1 ) or \
							   ( i+b<len(self.grid) and j-a+b>=0 and self.grid[i+b][j-a+b] == 1 ) or \
							   ( i+b<len(self.grid) and j+a-b<len(self.grid) and self.grid[i+b][j+a-b] == 1 ):
								currDist = a
								isFind = True
								break
						if isFind:
							break
				distData[(i,j)] = currDist

		distNeed = -1
		for _ in distData:
			if distData[_]>distNeed:
				distNeed = distData[_]

		print( distData )
		return distNeed

def do_main():
	n = 7

	grid = list()
	for i in range(n):
		line_data = list()
		for j in range(n):
			line_data.append( random.randint(0,1) )
		grid.append( line_data )

	# grid = [ [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0] ]

	for i in grid:
		print(i)
	print( Solution(grid).maxDistance() )

if __name__ == '__main__':
	do_main()
