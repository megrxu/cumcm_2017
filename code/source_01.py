# To get the suited vertices and matrix for further use

from init import *
from apps import *
import numpy


STD_DIS = 3 / 60 * 60 * 1000 / 100

# define const name, A, B, C, D, E, F or All
name = 'D'

# get the adjacency matrix
mat = map_region(nodes, lines, name)

# get the shortest distance array of every poliction station to every node
police, dist, prev , offset = police_distance(police, mat, name, )

V = len(mat)
P = len(police)

# find who suits the case
j = 0
suited = []
for i in dist:
  k = 0
  node_set = set()
  for dis in i:
    if (dis <= STD_DIS):
      node_set.add(k+offset)
    k=k+1
  suited.append(node_set)
  j = j+1

rows = police.shape[0] + 1
clos = dist[0].shape[0] + 1
output = numpy.zeros([rows, clos])
for i in range(rows):
  if (i >= 1):
    output[i, 1:] = dist[i-1]
node_index = numpy.arange(1, 583)
ran = get_row_index(name)
output[0, 1:] = node_index[ran[0]:ran[1]]
output[1:, 0] = police.astype(int)

numpy.savetxt("output/" + name + ".csv", output, delimiter=",")

# Type 1
set_01 = set(police)

# Type 2
node_set = set()
for item in suited:
  node_set = node_set.union(item)
set_02 = node_set - set(police)

# Type 3
set_03 = set(range(offset, offset + V)) - node_set

rate = nodes[4,:]