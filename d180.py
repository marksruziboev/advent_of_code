from time import perf_counter as pfc
from itertools import combinations

f = open('d18.txt', 'r').read().split('\n')

cent = []
for a in f:
	cent.append([int(b) for b in a.split(',')])
#print(cent)

def adds(a, b, c, d):
	return([(a[0]+b[0]+c[0]+d[0])*0.5, (a[1]+b[1]+c[1]+d[1])*0.5, (a[2]+b[2]+c[2]+d[2])*0.5])
#directions:
d = []
d.append([1, 1, 1])   #1
d.append([1, 1, -1])  #2
d.append([1, -1, 1])  #3
d.append([1, -1, -1]) #4
d.append([-1, 1, 1])  #5
d.append([-1, 1, -1]) #6
d.append([-1, -1, 1]) #7
d.append([-1, -1, -1]) #8
#faces of the cube


print(face)
