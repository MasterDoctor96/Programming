"""Python Morsels Exercise 21-02-2020"""

# def add(m1,m2):
# 	"""Return the matrix addition for m1 and m2"""

# 	if [len(lin_m1)==len(lin_m2) for lin_m1,lin_m2 in zip(m1,m2)]:
# 		return [[ele_m1 + ele_m2 for ele_m1, ele_m2 in zip(lin_m1, lin_m2)] for lin_m1, lin_m2 in zip(m1, m2)]
# 	else:
# 		raise ValueError('Expected equal size arguments')


def add(*matrices):
	"""Return the matrix addition for the arguments"""
	
	sizes = {tuple(len(row) for row in matrix) for matrix in matrices}

	if len(sizes) == 1:
		return [[sum(elements) for elements in zip(*rows)] for rows in zip(*matrices)]
	else:
		raise ValueError('Expected equal size arguments')
