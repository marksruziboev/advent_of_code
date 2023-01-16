import string 
import json

def worry(i, old):
	if i == 0:
		return(3*old)
	elif i ==1:
		return(19*old)
	elif i == 2:
		return(old+2)
	elif i == 3:
		return(old*old)
	elif i == 4:
		return(old+8)
	elif i == 5:
		return(old+6)
	elif i == 6:
		return(old+7)
	elif i == 7:
		return(old+4)
def wor(i, old):
	return((worry(i, old)%9699690)//3)
#X= 11*19*21*10*17*13
#print("X=", X)

#def trans(i):
div = [2, 7, 11, 19, 3, 5, 17, 13]
M =[]
M.append([66, 59, 64, 51])
M.append([67, 61])
M.append([86, 93, 80, 70, 71, 81, 56])
M.append([94])
M.append([71, 92, 64])
M.append([58, 81, 92, 75, 56])
M.append([82, 98, 77, 94, 86, 81])
M.append([54, 95, 70, 93, 88, 93, 63, 50])

N = [0, 0, 0, 0, 0, 0, 0, 0] 


f = open("d11.txt", 'r').read().split('\n')
for j in range(0, 10000):
	for k in range(0,8):
		if len(M[k])>0:
			for l in range(0, len(M[k])):
					a = M[k][0]
					M[k].remove(M[k][0])
					N[k] += 1
					if wor(k, a) % div[k] == 0:
						M[int(f[7*k+4].split(' ')[-1])].append(wor(k, a))
					else: 
						M[int(f[7*k+5].split(' ')[-1])].append(wor(k, a))

		

#print(M)
A = sorted(N)
print(A)
print(A[-1]*A[-2])
print(303*298)
