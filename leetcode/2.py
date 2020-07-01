#!/usr/bin/python3
# -*- coding:utf-8 -*-

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def print_node( head ):
	cnt = 0
	while head is not None:
		if cnt > 0:
			print( "->",end="" )
		print( head.val, end="" )
		head = head.next
		cnt += 1
	print( "" )

def init_node( data ):
	cnt = 0
	head = None
	for i in data:
		curr_node = ListNode(i)
		if cnt == 0:
			head = curr_node
		else:
			last_node.next = curr_node
			
		cnt += 1
		last_node = curr_node

	return head

class Solution:
	# def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
	def addTwoNumbers(self, l1, l2):
		res = []
		carry = 0

		while l1 is not None or l2 is not None:
			# print( l1.val,l2.val,carry )

			v1 = 0 if l1 is None else l1.val
			v2 = 0 if l2 is None else l2.val

			sum = v1 + v2 + carry
			carry = sum//10
			res.append(sum)
			if carry > 0:
				res[len(res)-1] -= 10

			l1 = l1.next if l1 is not None else None
			l2 = l2.next if l2 is not None else None

		if carry>0:
			res.append( carry )

		return init_node( res )

a = Solution()
# print_node( a.addTwoNumbers( init_node([2,4,3]),init_node([5,6,4]) ) )
print_node( a.addTwoNumbers( init_node([1]),init_node([9,9,1]) ) )
