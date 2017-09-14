# 0-1 Programming for another

from pulp import *
from apps import *
from init import *
import numpy as np

THEFT = 32
NAME = 'A'
STD_DIS = 10
X_PRE = 'x_'
MAX = 82

where_to_push = [1, 2, 3, 4, 5, 6, 7]

mat = map_region(nodes, lines, NAME)

# get the shortest distance array of every poliction station to every node
police, dist, prev , offset = police_distance(police, mat, NAME)

V = len(mat)
P = len(police)
I = len(where_to_push)

# Set objects
model  = LpProblem('model', LpMinimize)
X = np.empty([I, P]).astype(LpVariable)


keys = []
for i in range(I):
  for j in range(P):
    key = X_PRE + str(i) + '_' + str(j)
    X[i][j] = LpVariable(key, cat='Binary')
    keys.append(key)

# 载入约束变量
for j in range(P):
  model += sum(X[i][j] for i in range(I)) <= 1

for i in range(I):
  model += sum(X[i][j] for j in range(P)) == 1


# Find max
for j in list(range(P)):
  for i in list(range(I)):
    if (dist[j][where_to_push[i] - offset]):
      model += X[i][j] * dist[j][where_to_push[i] - offset]<= MAX

# Solve
print(model)
GLPK().solve(model)

# 显示结果

for i in model.variables():
    if i.varValue:
        arr = i.name.split('_')
        i ,j = int(arr[1]), int(arr[2])
        print('Police: ', police[j],'\tInout: ', where_to_push[i], '\tDistance: ', value(X[i][j] * dist[j][where_to_push[i] - offset]))