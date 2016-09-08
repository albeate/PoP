#
# opgave 6 "Game of Life"
#
#
from kursusuge6modul import *


def foerste():
	"""
	Defining a grid 
	input: imin, imax, jmax, jmin
	output: a grid
	"""
	return (0,50, 0, 50)

B = [(10,6), (10,7), (10,8), (9,8), (8,7)]
#B = [(40,40),(40,41),(40,42)]

# Defining the matrix to begin at False(dead cells) instead of True(living cells), this'll prove helpfull later in the code. 
matrix = [[False for i in range(foerste()[1]+1)] for j in range(foerste()[3]+1)] 
for b in B:
	matrix[b[0]][b[1]] = True


def naeste():
	"""
	Computes the neighbours of the given cells and whether or not the cells have to die, live or be rebourn
	& how the grid'll work with the growing cells. 
	"""
	global matrix # re-use the matrix that have been defined above, but has to remain in its form.  
	i_min, i_max, j_min, j_max = foerste() # instead of constantly call the function foearste() in the code. 
	n_matrix = [[False for j in range(j_max+1)] for i in range(i_max+1)] # defining a new matrix that may be altered. 
	for i in range(i_max+1): #
		for j in range(j_max+1): #
			n = 0 # count neighbours, at the start of zero. 

			# These loop tell our grid to be a "doughnut," (continueous) which means that when you hit
			# the boarder the cell formation will continue on the other side try the code.
			if i == i_min: 
				i_loop = [i_max,i,i+1]
			elif i == i_max:
				i_loop = [i-1,i,i_min]
			else:
				i_loop = [i-1,i,i+1]

			if j == j_min:
				j_loop = [j_max,j,j+1]
			elif j == j_max:
				j_loop = [j-1,j,j_min]
			else:
				j_loop = [j-1,j,j+1]

			
			"""
			This piece of code counts the number of neighbouring cells there are to the already living cells. 
			Everytime x and y equal   
			"""
			for x in i_loop: 
				for y in j_loop: 				
					if x == i and y ==j: 
						continue
						# When there's a new point (aka a new cell) the n'count will go up and 
						# run through the loop again until it reaches a certian count and will continue through the code 
					if matrix[x][y]: 
						n += 1

			# Defining the rules of the game
			# dead
			if (not matrix[i][j]) and (n == 3): # 3 neighbours, a dead cell'll be awaken
				n_matrix[i][j] = True
			# living 
			if matrix[i][j] and (n == 2 or n == 3): # 2 to 3 neighbours, the cell'll continue living 
				n_matrix[i][j] = True
	matrix = n_matrix
	return foerste()


def levende(i,j): 
	"""
	Returns the matrix of i and j 
	"""
	return matrix[i][j]

visLife(foerste,naeste,levende)
"""
Animates the "Game of Life" by calling the kursusuge6modul. ... & it's nicely awesome (Y) ;-)
"""
#testing the code.
if __debug__:
	print "Test1  af  levende(i,j) =", levende(i,j)==matrix[i][j]
	# testing if levende() returns the correct amount of cells in the first generation
	print "Test1 af naeste() =", naeste()==foerste() 
	# testing grid and counting of neighbouring cells 
	print "Test2 af levende(i,j) =", levende(i,j)==matrix[i][j]
	# testing if levende() returns the correct amount of cells in the first second generation
