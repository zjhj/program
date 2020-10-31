#!/usr/bin/python3
# -*- coding:utf-8 -*-

import collections
import random

class MyDeck:
	rank_data = list( map( str,range(2,11) ) ) + ['J','Q','K','A']
	suit_data = [ 'spades', 'hearts', 'clubs', 'diamonds' ]
	card = collections.namedtuple( 'Card', ['rank','suit'] )

	def __init__( self ):
		self._cards = [ self.card(i,j) for i in self.rank_data for j in self.suit_data ]
		# self._cards.append( self.card('black joker','') )
		# self._cards.append( self.card('red joker','') )

	def __len__( self ):
		return len( self._cards )
	
	def __getitem__( self,position ):
		return self._cards[position]


A = MyDeck()
# print( A[0] )
# print( len(A) )
# print( random.choice(A) )
# print( A[:-5] )

suit_values = dict( spades=3, hearts=2, diamonds=1, clubs=0 )
def spades_high( card ):
	rank_value = MyDeck.rank_data.index( card.rank )
	return rank_value*len(suit_values)+suit_values[card.suit]

for curr_card in sorted( A, key=spades_high ):
	print( curr_card )

"""
player_a = []
player_b = []
for i in range( len(cards)//2 ):
	player_a.append( random.choice(cards) )
	cards.remove( player_a[-1] )
player_b = cards

print( "A:" )
print( player_a )
print( "B:" )
print( player_b )
"""
