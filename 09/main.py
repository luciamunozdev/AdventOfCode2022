grid = [
['.','.','.','.','.','.',], # 00 01 02 03 04 05
['.','.','.','.','.','.',], # 10 11 12 13 14 15
['.','.','.','.','.','.',],	# 20 21 22 23 24 25
['.','.','.','.','.','.',], # 30 31 32 33 34 35
['H','.','.','.','.','.',]]	# 40 41 42 43 44 45

#print(grid)

gridT = [
['.','.','.','.','.','.',], # 00 01 02 03 04 05
['.','.','.','.','.','.',], # 10 11 12 13 14 15
['.','.','.','.','.','.',],	# 20 21 22 23 24 25
['.','.','.','.','.','.',], # 30 31 32 33 34 35
['.','.','.','.','.','.',]]

archivo = open("input.txt")


# create an empty list to store the instructions from the file
instructions = []

# read the lines from the file and add them to the list of instructions
while True:
    line = archivo.readline()

    # if there are no more lines to read, break out of the loop
    if not line:
        break

    line = line.split()
	# add the instruction to the list of instructions
    instructions.append((line[0], int(line[1])))

# hacer una funcion que devuelva true o false si hay un T al lado de un H, mirar tambien las diagonales
def findT(grid):
	res = False
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == 'H':
				if grid[i][j] == 'T':
					res = True
				elif i-1 >= 0 and grid[i-1][j] == 'T':
					res = True
				elif i+1 < len(grid) and grid[i+1][j] == 'T':
					res = True
				elif j-1 >= 0 and grid[i][j-1] == 'T':
					res = True
				elif j+1 < len(grid[i]) and grid[i][j+1] == 'T':
					res = True
				elif i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] == 'T':
					res = True
				elif i-1 >= 0 and j+1 < len(grid[i]) and grid[i-1][j+1] == 'T':
					res = True
				elif i+1 < len(grid) and j-1 >= 0 and grid[i+1][j-1] == 'T':
					res = True
				elif i+1 < len(grid) and j+1 < len(grid[i]) and grid[i+1][j+1] == 'T':
					res = True



	if (res == False):
		#find the pos where 'T' is and change it to '.'
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if grid[i][j] == 'T':
					grid[i][j] = '.'

	return res

# apply the instructions to the matrix and remove then once is done
print(instructions)
k = 1
r = 0
while instructions:
	direcc, moves = instructions[0]
	instructions.pop(0)
	isChange = False
	for i in range(len(grid)) :
	#start reading the grid from the left
		for j in range(len(grid[i])):
			#print('paso2')
			if (grid [i][j] == 'H' and isChange == False ):
				print('estoy pasando por ', k, ' vez')
				if direcc == 'U':
					q = 0
					while q < moves:
						if i-q-1 >= 0:
							if grid[i-q-1][j] == 'T':
								grid[i-q-1][j] = 'H'
								grid[i-q][j] = '.'
							else:
								grid[i-q-1][j] = 'H'
								grid[i-q][j] = '.'
								if findT(grid) == False:
									grid[i-q][j] = 'T'
									gridT[i-q][j] = '#'
									r += 1
							isChange = True
						q += 1

						
					isChange = True

				elif direcc == 'D':
					q = 0
					while q < moves:
						if i+q+1 < len(grid):
							if grid[i+q+1][j] == 'T':
								grid[i+q+1][j] = 'H'
								grid[i+q][j] = '.'
							else:
								grid[i+q+1][j] = 'H'
								grid[i+q][j] = '.'
								if findT(grid) == False:
									grid[i+q][j] = 'T'
									gridT[i+q][j] = '#'
									r += 1
							isChange = True
						q += 1

				elif direcc == 'L':
					q = 0
					while q < moves:
						if j-q-1 >= 0:
							if grid[i][j-q-1] == 'T':
								grid[i][j-q-1] = 'H'
								grid[i][j-q] = '.'
							else:
								grid[i][j-q-1] = 'H'
								grid[i][j-q] = '.'
								if findT(grid) == False:
									grid[i][j-q] = 'T'
									gridT[i][j-q] = '#'
									r += 1
							isChange = True
						q += 1

				elif direcc == 'R' :
						q = 0
						while q < moves:
							if j+q+1 < len(grid[i]):
							# si en algun momento 'H' se pone en donde esta 'T' entonces se cambia a '.'
								if grid[i][j+q+1] == 'T':
									grid[i][j+q+1] = 'H'
									grid[i][j+q] = '.'
								else:
									grid[i][j+q+1] = 'H'
									grid[i][j+q] = '.'
									if findT(grid) == False:
										grid[i][j+q] = 'T'
										gridT[i][j+q] = '#'
										r += 1
								isChange = True
							q += 1
						
				print('dirección: ', direcc, 'movimientos: ', moves)
				print(grid[0],'\n')
				print(grid[1],'\n')
				print(grid[2],'\n')
				print(grid[3],'\n')
				print(grid[4],'\n')
				k += 1
				print('tablero posiciones de T\n')
				print(gridT[0],'\n')
				print(gridT[1],'\n')
				print(gridT[2],'\n')
				print(gridT[3],'\n')
				print(gridT[4],'\n') 
				#print(instructions)
				break
			
		
					
print('tablero final\n')
grid[4][0] = 's'
print(grid[0],'\n')
print(grid[1],'\n')
print(grid[2],'\n')
print(grid[3],'\n')
print(grid[4],'\n') 

print('tablero posiciones de T\n')
#gridT[4][0] = 's'
print(gridT[0],'\n')
print(gridT[1],'\n')
print(gridT[2],'\n')
print(gridT[3],'\n')
print(gridT[4],'\n') 

#contar cuantas # hay en gridT
count = 0
for i in range(len(gridT)):
	for j in range(len(gridT[i])):
		if gridT[i][j] == '#':
			count += 1

print('cantidad de T: ', r)

archivo.close()