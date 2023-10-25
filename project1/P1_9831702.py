import numpy as np


def swap(matrix , i , j):

	matrix[[i, j]] = matrix[[j , i]]


def echlone(matrix , n , m):

	x = 0
	p = []
	for i in range(m):
		y = 0
		if abs(matrix[x][i]) == 0.0 :
			for j in range(x + 1 , n):
				if matrix[j][i] != 0.0 :
					y = 1
					swap(matrix , x , j)
					break
			if y == 0 :
				continue
		matrix[x] = matrix[x] * (1 / matrix[x][i])
		for j in range(x + 1 , n):
			matrix[j] += matrix[x] * -matrix[j][i]
		p.append((x , i))
		x += 1
		if x == n:
			break;
	return p

def RREF(matrix , p):

	for t in range(len(p) - 1 , -1 , -1):
		i, j = p[t]
		for r in range(i - 1 , -1 , -1):
			matrix[r] += matrix[i] *  -matrix[r][j]

#get inputs
n , m = map(int, input().split())
matrix = np.zeros((n , m))
for i in range(n):
	matrix[i] = list(map(float, input().split()))
p = echlone(matrix , n , m)
RREF(matrix , p)
x = np.ones(m) * 10

for t in range(len(p)):
		i, j = p[t]
		x[j] = 0
		for c in range(m - 1):
			if(c == j):
				continue
			x[j] += -x[c] * matrix[i][c]
		x[j] += matrix[i][m - 1]

#print answer
for i in range(n):
	for j in range(m):
		print(matrix[i][j] , end=" ")
	print()
for i in range(m - 1):
	print(f"X{i + 1}" , "=" , x[i])











