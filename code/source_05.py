
# from source_01 import *
from apps import *
from init import *

THEFT = 32
NAME = 'ALL'
STD_DIS = 10

mat = map_region(nodes, lines, NAME)
offset = get_row_index(NAME)[0]+1

dist, prev = dijkstra(mat, THEFT - offset)

time_dis = list(range(1,6))

all_where = []

prev_where = set()
for k in time_dis:
  now_where = set()
  for i,n in enumerate(dist):
    if (n < k * STD_DIS):
      now_where.add(i+offset)
  now_where = now_where - prev_where
  prev_where = now_where.union(prev_where)
  all_where.append(now_where)

for i,n in enumerate(all_where):
  print(i+1, ' & ' ,n)
  for i in n:
    m = prev[i-offset]
    arr = [i]
    string = str(i)
    while(m != -2):
      arr.append(int(m+offset))
      m = prev[int(m)]
    arr.reverse()
    # string = '$'
    # for i in range(len(arr)-1):
    #   string +=  str(arr[i]) + '\t\\to\t'
    # string += str(arr[len(arr)-1]) + '\t$'
    # print(string)