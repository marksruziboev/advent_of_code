import string 
import io

S = 0
f = open('input.txt', 'r')
buf = f.read() 
#print(buf)
st = buf.split('\n')
for z in st:
	c = z.index('-')
	k = z. index(',')
	n1 = int(z[:c])
	n2 = int(z[c+1:k])
	e = z.index('-', k+1)
	m1 = int(z[k+1:e])
	m2 = int(z[e+1:])
	#if (n1 <= m1 and n2 >= m2) or (m1 <= n1 and m2 >= n2): #this is for the first part
	#	S = S + 1 
	if (n1 >= m1 and n1 <= m2) or (m1 <= n2 and m2 >= n2):
		S = S + 1
		#print(z)
	elif (m1 > n1 and m1 < n2) or (n1 < m2 and n2 > m2):
		S = S + 1		
		#print(z)
f.close()

print(S)

