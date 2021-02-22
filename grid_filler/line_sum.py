'''line sum calculator

To Do:
	function that takes a list of numbers and a int, and returns a list of all combinations of sequential numbers in the list that sum to the target.

'''

def line_check_sum(search_space, target):
	temp_sum = 0
	res = []
	for i in range(len(search_space)):
		temp_sum = search_space[i]
		if temp_sum == target:
			res.append((i,i))
		for n in range(i+1,len(search_space)):
			if temp_sum <= target:
				temp_sum += search_space[n]
			if temp_sum > target:
				break
			if temp_sum == target:
				res.append((i,n))
	return res
