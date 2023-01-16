import string 

def qovin(arg):
	if (arg >= 65 and arg <= 90):
			return arg - 38
	elif (arg >= 97 and arg <= 122):
			return arg - 96

S = 0
i = 0 
#with open('input2.txt') as fil:
#	for lin in  fil:
#part1
#		n = int(len(lin)/2)
#		print(lin[:n])
#		print(lin[n:])
#		c = 0
#		for a in lin[:n]:
#			for b in lin[n:]:
#				if (a == b):
#					c = 1
#					print(a, "=", qovin(ord(a)))
#					S = S + qovin(ord(a))
#					break
#			if (c > 0):
#				break		
#part2
import io

f = open('input.txt', 'r')
buf = f.read() 
#print(buf)
st = buf.split('\n')
#print(st)
N = len(st)
for i in range(0, int(N/3)):
	#print(3*i)
	x = False
	for a in st[3*i]:
		y = False
		for b in st[3*i + 1]:
			#print(i+1)
			for c in st[3*i + 2]:
				#print(i)
				if (a == b and b == c): # a = b = c
					x = True
					y = True
					S = S + qovin(ord(a))
					#print(a)
					break
			if y:
				break
		if x:
			break	
f.close()

print(S)

