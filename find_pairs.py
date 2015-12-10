# input [1,2,4,3,5,6] 6
# output
# 1,5
# 2,4
	
	

def find_pairs(input_list, the_sum):
	
	input_list.sort()
	pair_dict = {}
	
	for i in input_list:
		diff = the_sum - i
		#print i 
		# print i in pair_dict.values()
		if diff in input_list and (not (i in pair_dict and diff in pair_dict.values()) and \
									not (diff in pair_dict and i in pair_dict.values())) and (i != diff):
			pair_dict[i] = diff
			#print str(i) + ',' + str(diff)
	
	if len(pair_dict) == 0:
		print 'No pairs found'
		return
	
	for pair in pair_dict:
		print str(pair) + "," + str(pair_dict[pair])
			
if __name__ == '__main__':
	input_list = [1,2,4,3,5,6]
	find_pairs(input_list, 1)
	#input_list = [-5,10,2,3,-1,6]
	#find_pairs(input_list, 4)
