import numpy as np
import apps
from PIL import Image
from math import acos, pi

RATIO = ((288 / 80) + (107 / 30)) / 2

cir_data = np.loadtxt('inputs/SplinedRound.csv', delimiter=',')
ell_data = np.loadtxt('inputs/SplinedEllipse.csv', delimiter=',')

apps.mat2img(ell_data).save('haha.png')

cir_index = []
ell_index = []
for i in range(180):
  cir_index.append(list(cir_data[:, i]).index(max(cir_data[:, i])))
  ell_index.append(list(ell_data[:, i]).index(max(ell_data[:, i])))

diff = (np.array(cir_index) - np.array(ell_index))

angles = []
for i in range(180):
  cos_value = diff[i] / 45 / RATIO / 1.01085271318
  angle_tmp = acos(cos_value) / pi * 180
  if (i == 0):
    angles.append(angle_tmp)
  elif (angle_tmp < angles[i-1]):
    angles.append(360 - angle_tmp)
  else:
    angles.append(angle_tmp)

np.savetxt('outputs/angles.csv', angles, delimiter=',')