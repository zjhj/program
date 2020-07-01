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
		res = curr_node = None
		carry = 0

		while True:
			if l1 is None or l2 is None:
				if l1 is None:
					curr_line = l2
				else:
					curr_line = l1

				curr_node = curr_line
				last_node.next = curr_node

				break
			else:
				curr_node = l1
				curr_node.val += l2.val

				if res is None:
					res = curr_node
				else:
					last_node.next = curr_node

				last_node = curr_node

				l1 = l1.next
				l2 = l2.next

		curr_node = res
		carry = 0
		while curr_node is not None:
			if carry > 0:
				curr_node.val += carry

			if curr_node.val >= 10:
				curr_node.val -= 10
				carry = 1
			else:
				carry = 0

			last_node = curr_node
			curr_node = curr_node.next

		if carry > 0:
			last_node.next = ListNode(carry)
				

		return res

a = Solution()
# print_node( a.addTwoNumbers( init_node([2,4,3]),init_node([5,6,4]) ) )
# print_node( a.addTwoNumbers( init_node([1]),init_node([9,9,1,2,2,2]) ) )
print_node( a.addTwoNumbers( init_node([5]),init_node([5]) ) )
