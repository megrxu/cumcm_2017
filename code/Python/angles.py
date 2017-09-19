import numpy as np
import apps
from PIL import Image
from math import acos, pi

# 取得放缩比
RATIO = ((288 / 80) + (107 / 30)) / 2

# 读入处理好的圆心及椭圆中心的轨迹
cir_data = np.loadtxt('inputs/SplinedRound.csv', delimiter=',')
ell_data = np.loadtxt('inputs/SplinedEllipse.csv', delimiter=',')

# 对轨迹进行坐标化，存入两个一维数组中
cir_index = []
ell_index = []
for i in range(180):
  cir_index.append(list(cir_data[:, i]).index(max(cir_data[:, i])))
  ell_index.append(list(ell_data[:, i]).index(max(ell_data[:, i])))

# 计算轨迹差值
diff = (np.array(cir_index) - np.array(ell_index))

# 计算180个方向的角度，并加入修正因子
angles = []
no = []
yes = []
for i in range(180):
  cos_value = diff[i] / 45 / RATIO / 1.01085271318
  no.append(cos_value * 1.01085271318)
  yes.append(cos_value)
  angle_tmp = acos(cos_value) / pi * 180
  if (i == 0):
    angles.append(angle_tmp)
  elif (angle_tmp < angles[i-1]):
    angles.append(360 - angle_tmp)
  else:
    angles.append(angle_tmp)

# 存储角度数据
np.savetxt('outputs/angles.csv', angles, delimiter=',')
np.savetxt('outputs/no.csv', no, delimiter=',')
np.savetxt('outputs/yes.csv', yes, delimiter=',')
