import re 
import string
import time

def oper(a):
	if a[1] == '+':
		return(val[a[0]] +val[a[2]])
	elif a[1] == '-':
		return(val[a[0]] - val[a[2]])
	elif a[1] == '*':
		return(val[a[0]] * val[a[2]])
	elif a[1] == '/':
		return(val[a[0]] // val[a[2]])
def fool(z):
	if z in val:
		return False
	else:
		return(True)

f = open('d212.txt', 'r').read().split('\n')
val = {} 
for a in f:
	if len(a.split(' ')) == 2:
		val[a.split(' ')[0][:4]] = int(a.split(' ')[-1]) 
val['humn']= 3952288690726# 0000 #5099000 
while (1):
	for a in f:
		if len(a.split(' ')) == 4 and  (a.split(' ')[1] in val) and (a.split(' ')[3] in val):
			#print(a.split(' ')[0][:4])
			val[a.split(' ')[0][:4]] = oper(a.split(' ')[1:4])
	if (len(val) == len(f)):
		break		
print(val['ddzt'])
print(val['rmtp'])
print(val['humn'])

		


#for a in f:
#	if a.startswith('root'):
#		val['root'] = a.split(' ')[1:]
#for a in f: 
#	if a.startswith(str(val['root'][0])):
#		val[val['root'][0][0:4]] = a.split(' ')[1: ]
#	if a.startswith(str(val['root'][2])):
#		val[val['root'][2][0:4]] = a.split(' ')[1: ]
#print(val)
#k = 0 
#while (k < 20):
#	val1 = {}
#	for b in val:
#		if (len(val[b]) == 3):
#			for c in val[b]:
#				#if fool(c) and len(c)>1:
#				for a in f:
#					if  a.startswith(str(c)):
#						val1[str(c)] = a.split(' ')[1: ]
#	val.update(val1)
#	k +=1
##for a in val:
#	if len(val[a]) == 1:
#print(val['ddzt'])
