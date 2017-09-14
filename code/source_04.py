# 0-1 Programming for another

from pulp import *
import numpy as np
from source_02 import *

X_PRE = 'x_'
MAX = 40

# Set objects
model  = LpProblem('model', LpMinimize)
X = np.empty([I, P]).astype(LpVariable)

keys = []
for i in range(I):
  for j in range(P):
    key = X_PRE + str(i) + '_' + str(j)
    X[i][j] = LpVariable(key, cat='Binary')
    keys.append(key)

# Load the constrains
for j in range(P):
  model += sum(X[i][j] for i in range(I)) <= 1

for i in range(I):
  model += sum(X[i][j] for j in range(P)) == 1



# Find max
for j in list(range(P)):
  for i in list(range(I)):
    if (dist[j][inout[i] - offset]):
      model += X[i][j] * dist[j][inout[i] - offset]<= MAX

# Solve
GLPK().solve(model)

# Show the result
result = []
for i in model.variables():
    if i.varValue:
        arr = i.name.split('_')
        i ,j = int(arr[1]), int(arr[2])
        result.append([police[j], inout[i], value(X[i][j] * dist[j][inout[i] - offset])])
        

#Sort the result and out put
result.sort(key=lambda x: x[2], reverse=True)
for i in result:
  print(i[0],'&', i[1], '&', "%.3f" % i[2], '\\\\')
print("Max Distance: ", "%.3f" % result[0][2])
