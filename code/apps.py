from xlrd import open_workbook
from xlrd import XL_CELL_TEXT, XL_CELL_NUMBER, XL_CELL_DATE, XL_CELL_BOOLEAN
import numpy as np
import math
from PIL import Image

def sheet_to_array(
        filename,
        sheet_number,
        first_col=0,
        last_col=None,
        header=True):
    """Return a floating-point numpy array from sheet in an Excel spreadsheet.

    Notes:
    0. The array is empty by default; and any non-numeric data in the sheet will
       be skipped.
    1. If first_col is 0 and last_col is None, then all columns will be used,
    2. If header is True, only one header row is assumed.
    3. All rows are loaded.
    """
    DEBUG = False
    # sheet
    book = open_workbook(filename)
    sheet0 = book.sheet_by_index(sheet_number)
    rows = sheet0.nrows
    # cols
    if not last_col:
        last_col = sheet0.ncols
    if first_col > last_col:
        raise Exception("First column must be smaller than last column!")
    cols = [col for col in range(first_col, last_col + 1)]
    # rows
    skip = 0
    if header:
        skip = 1
    data = np.empty([len(cols), rows - skip])

    for row in range(skip, sheet0.nrows):
        row_values = sheet0.row(row)
        for col, cell in enumerate(row_values):
            if DEBUG and row < 2:
                print(row, col, cell.ctype, cell.value, '\n')
            if col in cols and cell.ctype == XL_CELL_NUMBER:
                data[col - first_col, row - skip] = cell.value
    return np.transpose(data)

def mat2img(mat):
    return Image.fromarray((mat / np.amax(mat) * 255).astype(np.uint8))

def img2mat(img):
    return np.array(img)

def find_mid_index(value, li):
    first_index = li.index(value)
    last_index = first_index + 1
    n = len(li)
    while(li[last_index] == value and last_index < n):
        last_index += 1
    return int((last_index + first_index) / 2)

