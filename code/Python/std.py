# from init import sheet_01
import numpy as np
import apps
from PIL import Image

# 定义分辨率

sheet_01 = np.loadtxt('inputs/new_model_02.csv', delimiter=',')

res = 10

# 定义画板
board = np.zeros([180, 512 * res])

# 定义偏离值
offset_x = -24
offset_y = 32
sq = np.zeros([512, 512])
sq[128+offset_x:offset_x+256+128, 128+offset_y:offset_y+256+128] = sheet_01
tmp_img = apps.mat2img(sq).resize([512 * res, 512 * res])

# 模拟扫描
phase = 29.4056213110678
angle = 0.9996
tmp_img = tmp_img.rotate(-90 + phase)
for j in range(180):
  tmp_img = tmp_img.rotate(angle)
  tmp_mat = apps.img2mat(tmp_img)
  board[j] = tmp_mat.sum(1)

img_cat = np.transpose(board)[64*res:448*res, :]

img = apps.mat2img(img_cat).resize([180, 512])
img.save('outputs/new_model_02.png')
np.savetxt('outputs/new_model_02.csv', apps.img2mat(img), delimiter=',')