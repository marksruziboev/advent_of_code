from collections import defaultdict
import sys


f = open('d12.txt', 'r').read().split('\n')
#print(f[20][119])
def endp(f):
	i = -1
	for a in f:
		i += 1
		if a.find('E') != -1:
			return (i, a.find('E'))
#print(endp(f))

queue = []
queue.append(endp(f))
print(queue)