# Frequently used functions

import os
import platform
from xlrd import open_workbook
from xlrd import XL_CELL_TEXT, XL_CELL_NUMBER, XL_CELL_DATE, XL_CELL_BOOLEAN
import numpy as np
import math

INFINITY = -1
UNDIFINED = -2


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
    return data


def get_row_index(x):
    return {
        'A': [0, 92],
        'B': [92, 165],
        'C': [165, 319],
        'D': [319, 371],
        'E': [371, 474],
        'F': [474, 582],
        'ALL': [0, 582]
    }[x]

def get_police_index(x):
    return {
        'A': [0, 20],
        'B': [20, 28],
        'C': [28, 45],
        'D': [45, 54],
        'E': [54, 69],
        'F': [69, 80],
        'ALL': [0, 80]
    }[x]

def map_region(data, lines, name):
    row_index = get_row_index(name)
    nodes = data[0:3, row_index[0]:row_index[1]]
    j = row_index[1] - row_index[0]
    mat = np.ones([j, j]) * INFINITY

    for i in range(mat.shape[1]):
        mat[i, i] = 0
    for i in range(lines.shape[1]):
        if ((lines[0, i] >= nodes[0, 0]) and (lines[0, i] <= nodes[0, j - 1])
                and (lines[1, i] >= nodes[0, 0]) and (lines[1, i] <= nodes[0, j - 1])):
            # print(lines[0, i], lines[1, i])
            # print(lines[0, i] - row_index[0] - 1,
            #       lines[1, i] - row_index[0] - 1)
            # print((data[1, int(lines[0, i] - 1)], data[1, int(lines[1, i] - 1)],
            #        data[2, int(lines[0, i] - 1)], data[2, int(lines[1, i] - 1)]))
            distance = math.hypot(data[1, (lines[0, i] - 1)] - data[1, (
                lines[1, i] - 1)], data[2, (lines[0, i] - 1)] - data[2, (lines[1, i] - 1)])
            # print(distance)
            mat[(lines[0, i] - row_index[0] - 1),
                (lines[1, i] - row_index[0] - 1)] = distance
            mat[(lines[1, i] - row_index[0] - 1),
                (lines[0, i] - row_index[0] - 1)] = distance
    return mat


def dijkstra(mat, node):
    # intial
    size = mat.shape[0]
    dist = np.ones(size) * INFINITY
    prev = np.ones(size) * UNDIFINED
    dist[node] = 0

    vertex_set = set(np.arange(0, size))
    # vertex_set.discard('')

    # dijkstra
    while len(vertex_set):
        for i in range(size):
            if (i in vertex_set and dist[i] >= 0):
                u = i
                break
        for i in vertex_set:
            if (dist[i] < dist[u] and dist[i] != -1):
                u = i
        vertex_set.discard(u)

        for v in range(size):
            if (mat[v, u] >= 0):
                alt = dist[u] + mat[v, u]
                if (alt < dist[v] or dist[v] == INFINITY):
                    dist[v] = alt
                    prev[v] = u

    # return result
    return dist, prev

def police_distance(data, mat, name, police=None):
    police_row = get_police_index(name)
    row = get_row_index(name)
    offset = row[0] + 1

    # get police indexes
    if (police == None):
        police = data[1, police_row[0]:police_row[1]]
        police = police.astype(int)
    else:
        tmp = data[1, police_row[0]:police_row[1]]
        tmp = set(tmp.astype(int))
        police = tmp.union(police)

    dis_arr = []
    pre_arr = []

    # dijastra
    for i in police:
        dist, prev = dijkstra(mat, i - offset)
        dis_arr.append(dist)
        pre_arr.append(prev)
    return police, dis_arr, pre_arr, offset

def police_inout(data, mat, input, name):
    police_row = get_police_index(name)
    row = get_row_index(name)
    offset = row[0] +1

    # get police indexes
    police = data[1, police_row[0]:police_row[1]]
    police = police.astype(int)

    dis_arr = []
    pre_arr = []
    for i in police:
        dist, prev = dijkstra(mat, i - offset)
        dis_arr.append(dist)
        pre_arr.append(prev)
    return police, dis_arr, pre_arr, offset

def near_index(dist, offset, i):
    arr = []
    for item in dist:
        arr.append(item[i])
    return arr.index(min(arr))

def suit_index(suited, i, offset):
    k = 0
    result = []
    for item in suited:
        if (i+offset) in item:
            result.append(k)
        k += 1
    return result

def myabs(num):
    return num if num >= 0 else -1 * num

def mymax(arr):
    max_tmp = arr[0]
    for i in arr:
        if (i >= max_tmp):
            max_tmp = i
    return max_tmp