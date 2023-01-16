from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
from functools import reduce
from bisect import bisect_left, bisect_right

#stone 1
st = []
st.append([['#', '#', '#', '#'], 1])
st.append([[['.', '#', '.'], ['#', '#', '#'], ['.', '#', '.']], 3])
st.append([[['.', '.', '#'], ['.', '.', '#'], ['#', '#', '#']], 3])
st.append([[['#'], ['#'], ['#'], ['#']], 4])
st.append([[['#', '#'], ['#', '#']], 2])
for a in st:
   print(a)
 
#board
display = []

f = open('d17.txt', 'r').read()
print(len(f))

for i in range(0, 2022):
    fs = st[i % 5][0]
    print(fs)

