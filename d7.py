import re


N = 1102
f = open('d7.txt', 'r').read().split('\n')
for i in range(0, N):
    if (f[i].startswith('$ cd') and f[i] != '$ cd ..'):
        j = 0
        while(f[i+j] != '$ cd'): 
            if (f[i].startswith('dir')):
                print(f[i].split(' ')[-1] + '/' + f[i+j].split(' ')[-1])
            j+= 1
#.startswith('dir')):

   