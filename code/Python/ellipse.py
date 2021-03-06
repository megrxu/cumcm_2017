from init import sheet_02
import numpy as np
import apps
from PIL import Image

# 找到椭圆的投影
vexs = []
for i in range(180):
  tmp = []
  for j in range(1, 512):
    if (sheet_02[j, i] != 0 and sheet_02[j-1, i] == 0):
      tmp.append(j)
    elif (sheet_02[j, i] == 0 and sheet_02[j-1, i] != 0):
      tmp.append(j-1)
  if (len(tmp)>2):
    if (tmp[1] - tmp[0] > tmp[3] - tmp[2]):
      tmp.remove(tmp[3])
      tmp.remove(tmp[2])
    else:
      tmp.remove(tmp[0])
      tmp.remove(tmp[0])
  vexs.append(list(tmp))

# 计算每个投影的最大长度
length = []
for item in vexs:
  length.append((item[1] - item[0]))

# 计算长轴与短轴的坐标和数值
max_axis = max(length)
min_axis = min(length)

max_index = apps.find_mid_index(max_axis, length)
min_index = apps.find_mid_index(min_axis, length)

print(max_axis, min_axis)
print(max_index, min_index)
