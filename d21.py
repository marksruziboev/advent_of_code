import re 
import string

def oper(a):
	if a[1] == '+':
		return(val[a[0]] +val[a[2]])
	elif a[1] == '-':
		return(val[a[0]] - val[a[2]])
	elif a[1] == '*':
		return(val[a[0]] * val[a[2]])
	elif a[1] == '/':
		return(val[a[0]] / val[a[2]])

f = open('d21.txt', 'r').read().split('\n')
val = {} 
for a in f:
	if len(a.split(' ')) == 2:
		val[a.split(' ')[0][:4]] = int(a.split(' ')[-1]) 
while (1):
	for a in f:
		if len(a.split(' ')) == 4 and  (a.split(' ')[1] in val) and (a.split(' ')[3] in val):
			#print(a.split(' ')[0][:4])
			val[a.split(' ')[0][:4]] = oper(a.split(' ')[1:4])
	if (len(val) == len(f)):
		break		
print(int(val['root']))
print(int(val['humn']))
