# The BIBD, Balanced Incomplete Block Design, Program!! Wuuhuu this is getting awesome... or not 
# 
# by Sarah & B!:)
#
# This program deals with lists in a list that can be catagorized as a BIBD which if 
# thats the case, the program will return TRUE. Otherwise, it'll return False. 
#
# We assume that a BIBD system shall be made up of at least to lists in a list.
#
xrr = [[1,2,3], [4,5,6], [7,8,9]


# The three function below are helpfunctions to compute the main function is_BS at the bottom.

def compare(xrr):
	"""
	This function compares the lenght of the lists in the list. 
	input: list of a list 
	output: same lenght -> True, not same lenght -> False 
	"""	
	for l in xrr: 
		if len(xrr[0]) != len(l):
		    return False
	return True



def duplicates(xrr):
	"""
	This function checks for duplicates of elements in the lists. 
	input: lists of a list 
	output: no duplicates -> True, duplicates -> False
	"""
	V = []
	for l in xrr:
		for e in l:
			if not (e in V):
				V.append(e)
	for e in V: 
		for l in xrr: 
			if l.count(e) > 1:
				return False
	return True 


def samepair(xrr):
	"""
	This function checks if any of the lists, in the list, contains the same elements.
	input: lists of a list 
	output: no same elementes in two lists -> True, same elements in two or more list -> False
	"""	
	for e in range(len(xrr)):
		for l in range(e+1, len(xrr)): 
			g = 0 
			V = []
			for k in xrr[e]:
				V.append(k)
			for c in xrr[l]:
				if c in V:
					g += 1
					if g > 1:
						return False
	return True


def is_BS(xrr):
	"""
	This function computes whether or not the list of the lists provided is a BIBD. 
	"""
	if compare(xrr) and duplicates(xrr) and samepair(xrr) == True:
		return True
	return False
print 'BIBD?:'
print is_BS(xrr)
print 
print 'OMG!? ...it works (^-^*)/'


