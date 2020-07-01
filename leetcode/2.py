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

		while l1 is not None and l2 is not None:
			print( l1.val,l2.val,carry )

			sum = l1.val+l2.val+carry
			carry = sum//10
			res.append(sum)
			if carry > 0:
				res[len(res)-1] -= 10

			l1 = l1.next
			l2 = l2.next

		if l1 is None and l2 is None and carry>0:
			res.append( carry )

		if l1 is None:
			while l2 is not None:
				sum = l2.val + carry
				carry = sum//10
				res.append(sum)
				if carry > 0:
					res[len(res)-1] -= 10
				l2 = l2.next
		else:
			while l1 is not None:
				sum = l1.val + carry
				carry = sum//10
				res.append(sum)
				if carry > 0:
					res[len(res)-1] -= 10
				l1 = l1.next

		return init_node( res )

a = Solution()
# print_node( a.addTwoNumbers( init_node([2,4,3]),init_node([5,6,4]) ) )
print_node( a.addTwoNumbers( init_node([3]),init_node([1,8]) ) )
