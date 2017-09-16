from init import sheet_01
import numpy as np
import apps
from PIL import Image

res = 1

board = np.zeros([180, 512 * res])

offset_x = 0
offset_y = 0
sq = np.zeros([256, 256])
sq[offset_x:offset_x+256, offset_y:offset_y+256] = sheet_01
tmp_img = apps.mat2img(sq).resize([512 * res, 512 * res])
tmp_img.save('test.png')

tmp_img = tmp_img.rotate(-90)
for j in range(180):
  tmp_img = tmp_img.rotate(1)
  tmp_mat = apps.img2mat(tmp_img)
  board[j] = tmp_mat.sum(1)

img = apps.mat2img(np.transpose(board)).resize([180, 512])
img.save('outputs/std.jpg')