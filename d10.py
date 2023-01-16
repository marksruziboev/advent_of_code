import re


f = open("d10.txt", 'r').read().split('\n')

def gir(f):
	c = 0
	p = 0
	X =[]
	for a in f:
		if a.startswith('noop'):
			X.append([c, p])
			c += 1
		elif a.startswith('add'):
			X.append([c, p])
			c += 1
			X.append([c, p])
			c += 1
			p = (p + int(a.split(' ')[-1])) % 40
	return(X)

p = 0
c = 0

#print(gir(f))
#print(len(gir(f)))
#LOOP WULD HAVE BEEN A BETTER SOLUTION HERE :))
str1 = ''
str2 = ''
str3 = ''
str4 = ''
str5 = ''
str6 = ''
for i in range(0,40):
	if (gir(f)[i][0] < gir(f)[i][1] or gir(f)[i][0] > gir(f)[i][1]+2):
		str1 += '.'
	elif (gir(f)[i][0] % 40 > gir(f)[i][1] or gir(f)[i][0] % 40 < gir(f)[i][1]+2):
		str1 += '@'
for i in range(40,80):
	if (gir(f)[i][0] % 40 < gir(f)[i][1] or gir(f)[i][0] % 40 > gir(f)[i][1]+2):
		str2 += '.'
	elif (gir(f)[i][0]% 40 > gir(f)[i][1] or gir(f)[i][0]% 40 < gir(f)[i][1]+2):
		str2 += '@'
for i in range(80,120):
	if (gir(f)[i][0] % 40< gir(f)[i][1] or gir(f)[i][0]% 40 > gir(f)[i][1]+2):
		str3 += '.'
	elif (gir(f)[i][0]% 40 > gir(f)[i][1] or gir(f)[i][0] % 40< gir(f)[i][1]+2):
		str3 += '@'
for i in range(120,160):
	if (gir(f)[i][0] % 40< gir(f)[i][1] or gir(f)[i][0] % 40> gir(f)[i][1]+2):
		str4 += '.'
	elif (gir(f)[i][0] % 40> gir(f)[i][1] or gir(f)[i][0]% 40 < gir(f)[i][1]+2):
		str4 += '@'
for i in range(160,200):
	if (gir(f)[i][0] % 40< gir(f)[i][1] or gir(f)[i][0]% 40 > gir(f)[i][1]+2):
		str5 += '.'
	elif (gir(f)[i][0] % 40> gir(f)[i][1] or gir(f)[i][0]% 40 < gir(f)[i][1]+2):
		str5 += '@'
for i in range(200,240):
	if (gir(f)[i][0]% 40 < gir(f)[i][1] or gir(f)[i][0]% 40 > gir(f)[i][1]+2):
		str6 += '.'
	elif (gir(f)[i][0]% 40 > gir(f)[i][1] or gir(f)[i][0] % 40< gir(f)[i][1]+2):
		str6 += '@'

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)


g = open("result.txt", 'a')
g.write(str1)
g.write(str2)
g.close()