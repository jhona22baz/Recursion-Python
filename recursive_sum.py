
def recursive_sum(MyList):
	'''	
	a short function of recursion list sum 
	'''
	total = 0
	for element in MyList:
		if type(element) == type([]):
			total = total + recursive_sum(element)
		else:
			total = total + element

	return total

diferent_list = [1,2,[3,4],5]
print recursive_sum(diferent_list) 