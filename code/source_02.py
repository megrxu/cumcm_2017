from init import *
from apps import *

# define const name to 'A', for we only consider the rigion A
name = 'ALL'

# # get the adjacency matrix
mat = map_region(nodes, lines, name)

# # get the shortest distance array of every poliction station to every node
police, dist, prev , offset = police_distance(police, mat, name)

# format and validation
inoutA = inoutA[0].astype(int)
inoutCity = inoutCity[0].astype(int)
tmp = []
for i in inoutA:
  if (i > 0):
    tmp.append(i)
inoutA = list(tmp)

tmp = []
for i in inoutCity:
  if (i != 0):
    tmp.append(i)
inoutCity = tmp

inoutCus = [37, 5, 6, 237, 16, 35, 36]


inout = inoutCus

I = len(inout)
P = len(police)
V = len(mat)
