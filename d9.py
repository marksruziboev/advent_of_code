import re 
import string

def adds(a, b):
	return([a[0]+b[0], a[1]+b[1]])

def sign(c):
	if(c > 0):
		return(1)
	elif(c<0):
		return(-1)
	else:
		return(0)

def inc(b, a):
	return([sign(b[0]-a[0]), sign(b[1]-a[1])])

def dst(a, b):
	return(max(abs(a[0]-b[0]), abs(a[1]-b[1])))
def dx(a, b):
	return(abs(a[0]-b[0]))
def dy(a,b):
	return(abs(a[1]-b[1]))


#directions
d = {'L':[-1, 0], 'U':[0, 1], 'R':[1, 0],'D':[0,-1]}
#initial postion
H = [0, 0]
T = [0, 0]
post = [(0,0)]
posh = [(0,0)]

f = open('d9.txt', 'r').read().split('\n')
N = len(f)
for i in range(0, N):
	a = f[i].split(' ')
	j = 0
	while (j < int(a[-1])):
		H = adds(H, d[a[0]])
		if dst(H, T) == 2:
			T = adds(T, inc(H, T))
			TT = (T[0], T[1])
			if TT not in post:
				post.append(TT)
		HH = (H[0], H[1])
		if HH not in posh:
				posh.append(HH)
		j = j +1
#print(posh)
print(len(post))



