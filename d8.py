import re


f = open('d8.txt', 'r').read().split('\n')
N = len(f[0])
V = 2*(N + N-2) #visible
print(V)
for i in range(1, N-1):
	for j in range(1, N-1):
		add = 0
		k = j-1
		while (int(f[i][j]) > int(f[i][k]) and k >= 0):
			k=k-1
		if(k == -1): #visible from left
			#print((i,j))
			add = 1
		k = j+1
		while (int(f[i][j]) > int(f[i][k]) and k < N-1):
		#	print(k)
			k=k+1
		if (k == N-1):# and int(f[i][j]) > int(f[i][N-1])):
			#print((i,j)) #visible from right
			add = 1 
		k = i-1
		while (int(f[i][j]) > int(f[k][j]) and k >=0):
			k=k-1
			if (k == -1):
				#print((i,j))
				add = 1 #visible from above
				z = 0
		#if (x==1 and y ==1 and z ==1):
		k = i+1
		while (int(f[i][j]) > int(f[k][j]) and k < N-1):
			k=k+1
		if (k == N-1 and int(f[i][j]) > int(f[N-1][j])):
			#print((i,j))
			add = 1 #visible from below
		V = V+add
print(V)

