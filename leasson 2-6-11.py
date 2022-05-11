n = int(input())
matrix = [[0 for i in range(n)] for j in range(n)]
a = 0
b = 0
c = 1
while matrix[a][b] == 0:
	if  b < (n-1) and a >= 0 and matrix[a][b+1] == 0:
		while b < (n-1) and a >= 0 and matrix[a][b+1] == 0:
			matrix[a][b] = c
			b += 1
			c += 1
	elif  b <= (n-1) and a < (n-1) and matrix[a+1][b] == 0:
		while b <= (n-1) and a < (n-1) and matrix[a+1][b] == 0:
			matrix[a][b] = c
			a += 1
			c += 1
	elif a <= (n-1) and b >= 0 and matrix[a][b-1] == 0:
		while a <= (n-1) and b >= 0 and matrix[a][b-1] == 0:
			matrix[a][b] = c
			b -= 1
			c += 1
	elif a >= 0 and b >= 0 and matrix[a-1][b] == 0:
		while a >= 0 and b >= 0 and matrix[a-1][b] == 0:
			matrix[a][b] = c
			a -= 1
			c += 1
	else:
		matrix[a][b] = c
		break
for i in matrix:
	for j in i:
		print(j, end=" ")
	print()