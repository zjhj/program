#!/usr/bin/python3
# 密码和每个数字，存在一位相同的情况（位置及数字均相同）
# 没结果？

data = [ '14073','63136','29402','35862','84271','79588','42936','98174','50811','07145' ]

for i in range(100000):
	"""
	if i!=39176:
		continue
	"""

	curr_cipher = "{:0>5d}".format(i)
	print( "curr_cipher: {}".format(curr_cipher) )

	not_find = False
	match_total = 0

	for curr_data in data:
		match_cnt = 0
		for j in range( len(curr_cipher) ):
			print( curr_data[j],curr_cipher[j] )
			if curr_data[j] == curr_cipher[j]:
				if curr_data.count(curr_data[j]) == 1:
					match_cnt += 1
				else:
					match_cnt = -1
					break
		print( "match_cnt: {}".format(match_cnt) )
		if match_cnt != 1:
			not_find = True
			break
		match_total += 1

		if match_total > 6:
			input()

	if not not_find:
		print( "Find!" )
		break
