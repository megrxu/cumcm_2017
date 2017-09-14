# 0-1 Programming

from pulp import *
import numpy as np
from source_01 import *
import csv
# from source_02 import *

X_PRE = 'x_'

# 设置对象
model  = LpProblem('model', LpMinimize)
X = np.empty([V, P]).astype(LpVariable)

keys = []
for i in range(V):
  for j in range(P):
    key = X_PRE + str(i) + '_' + str(j)
    X[i][j] = LpVariable(key, cat='Binary')
    keys.append(key)

# 目标函数
model += sum((sum((X[i][j] * dist[j][i]) for i in range(V))) for j in range(P)), 'profit'


# 载入约束变量
for i in range(V):
    flag = 1
    for j in range(P):
        if (i+offset in set_01):
            model += X[i][j] == (i == j)
        elif (i+offset in set_02):
            if (flag):
                set_tmp = set(suit_index(suited, i, offset))
                model += sum(X[i][j] for j in set_tmp) == 1
                model += sum(X[i][j] for j in set(range(P)) - set_tmp) == 0
                flag = 0
        elif (i+offset in set_03):
            model += X[i][j] == (j == near_index(dist, offset, i))

# Solve
GLPK().solve(model)

keys = set()
rate_average = sum(rate[offset-1:V+offset-1]) / P
jurisdiction = [set() for _ in range(P)]

each_node = []
for i in model.variables():
    if i.varValue:
        arr = i.name.split('_')
        i ,j = int(arr[1]), int(arr[2])
        jurisdiction[j].add(i+offset)
        each_node.append([i + offset, j+offset, dist[j][i]])

each_node.sort(key=lambda x: x[2], reverse=True)

k = offset
su = 0
each_police = []
for i in jurisdiction:
    diff = (sum(rate[k-1] for k in i) - rate_average)
    each_police.append([k, diff])
    k+= 1
    su += diff

each_police.sort(key=lambda x: x[1], reverse=True)


# Output

text_01 = []
text_02 = []

for i in each_node:
    text_01.append(('Node', i[0],'Police', i[1], 'Distance', "%.3f" % i[2]))

for i in each_police:
    text_02.append(("Police", i[0] , 'Diff', "%+.3f" % i[1] , 'Ave', rate_average))


text_02

with open('output/nodes/' + name + '_nodes.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(text_01)
    f_csv.writerows(text_02)
    f_csv.writerow(('Sum Distance', value(model.objective)))