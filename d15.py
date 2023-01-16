import string
f = open('ex.txt', 'r').read().split('\n')

def dst(a, b):
	return(abs(a[0] - b[0]) + abs(a[1] - b[1]))

S = []
B = []
for a in f:
	b = a.split(' ')
	#print(b)
	#sensor is at (b[2], b[3]) and beacon is at (b[8], b[9])
	S.append([int(b[2].split('=')[1][:-1]), int(b[3].split('=')[1][:-1])])
	B.append([int(b[8].split('=')[1][:-1]), int(b[9].split('=')[1])])
print(S[0])
print(S[0][0])

xmax = max(S[i][0]+dst(S[i], B[i]) for i in range(0, len(S)))
xmin = min(S[i][0]-dst(S[i], B[i]) for i in range(0, len(S)))
ymax = max(S[i][1]+dst(S[i], B[i]) for i in range(0, len(S)))
ymin = min(S[i][1]-dst(S[i], B[i]) for i in range(0, len(S)))
#print("xmin =", xmin, "xmax =", xmax, "ymin =", ymin, "ymax =", ymax)

#we shift x direction t te right by -xmin and y direction up (again) by -ymin
for i in range(0, len(S)):
	S[i][1] = S[i][1] - ymin
	B[i][1] = B[i][1] - ymin
	S[i][0] = S[i][0] - xmin
	B[i][0] = B[i][0] - xmin
#new range for xmax and ymax
nxmax = max(S[i][0]+dst(S[i], B[i]) for i in range(0, len(S)))
nymax = max(S[i][1]+dst(S[i], B[i]) for i in range(0, len(S)))
print("xmax =", xmax, "ymax =", ymax)
#everything will be printed on the box (0, nxmax)\times(0, nymax)

plt = [[]]
for k in range(0, nxmax):
	for l in range(0, nymax):
		if S.count([k,l]):
			plt.append('S')
		elif B.count([k, l]):
			plt.append('B')
		else:
			plt.append(0) 
print(len(plt))
