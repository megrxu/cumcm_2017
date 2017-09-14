from init import *
from apps import *

# define const
name = 'F'

# test mat
mat = map_region(nodes, lines, name)

# test dj
# mat = np.ones([5, 5]) * -1
# for i in range(mat.shape[1]):
#     mat[i, i] = 0
# mat[1, 0] = mat[0, 1] = 1
# mat[1, 3] = mat[3, 1] = 2
# mat[2, 3] = mat[3, 2] = 3
# mat[1, 2] = mat[2, 1] = 3
# mat[2, 4] = mat[4, 2] = 1
# mat[4, 3] = mat[3, 4] = 1

# test log

result = dijkstra(mat, 1)

dis_arr = police_distance(police, mat, lines, name)
print(dis_arr)

# print(mat)
