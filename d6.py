import re

l= open("d6.txt").read()


i= 0
while  i < len(l)-13:
    j = 0
    while j < 14:
        k = 1
        x = 0
        while k < 14-j:
            if l[i+j] == l[i+j+k]:
                x = 1
                break
            else:
                k = k+1;
        if (x):
            break
        j =j+1;
    if (j == 14):
        print(i+14)
        break
    i = i+1
    




           #z=s[:]
#for i in d:
 #   a,f,t=i[0],i[1]-1,i[2]-1
  #  s[t]=s[f][:a][::-1]+s[t]
   # s[f]=s[f][a:]
    #z[t]=z[f][:a]+z[t]
    #z[f]=z[f][a:]

#f = open("input.txt", "a")
#f.write("".join(x[0]for x in s)) 
#f.write("".join(x[0]for x in z))
#f.close()

#print("".join(x[0]for x in s))
#print("".join(x[0]for x in z))