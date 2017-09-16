import apps
import numpy as np

FILE_NAME = './A_attachment.xls'

sheet_01 = apps.sheet_to_array(
    FILE_NAME,
    0,
    first_col=0,
    last_col=255,
    header=False)

sheet_02 = apps.sheet_to_array(
    FILE_NAME,
    1,
    first_col=0,
    last_col=179,
    header=False)

sheet_03 = apps.sheet_to_array(
    FILE_NAME,
    2,
    first_col=0,
    last_col=179,
    header=False)

sheet_04 = apps.sheet_to_array(
    FILE_NAME,
    3,
    first_col=0,
    last_col=1,
    header=False)

sheet_05 = apps.sheet_to_array(
    FILE_NAME,
    4,
    first_col=0,
    last_col=179,
    header=False)

# test = apps.mat2img(sheet_02)
# test.save('out.jpg')

# Save csvs
np.savetxt('outputs/sheet_02.csv', sheet_02, delimiter=',')
np.savetxt('outputs/sheet_03.csv', sheet_03, delimiter=',')
np.savetxt('outputs/sheet_05.csv', sheet_05, delimiter=',')
