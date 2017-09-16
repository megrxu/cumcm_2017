import numpy as np
import apps
from PIL import Image
from math import asin, pi

cir_data = np.loadtxt('inputs/SplinedRound.csv', delimiter=',')

indexes = []
for i in range(180):
  for j in range(512):
    if (cir_data[j, i]):
      break
  indexes.append(j)
  # angles.append(asin((j - OFFSET)/AMP))

TIM = (149 - 61 + 1) * 4
MAX_INDEX = indexes.index(min(indexes))
OFFSET = indexes[int(MAX_INDEX - TIM/4)]
AMP = OFFSET - indexes[MAX_INDEX]

angles = []
for i in range(180):
  angle_tmp = (asin((OFFSET - indexes[i])/AMP))/pi*180
  if (i==0):
    angles.append(angle_tmp)
  elif angle_tmp > angles[i-1]:
    angles.append(angle_tmp)
  else:
    angles.append(180 - angle_tmp)

np.savetxt('outputs/angle.csv', angles, delimiter=',')
