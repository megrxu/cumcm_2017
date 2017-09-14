import apps

nodes = apps.sheet_to_array(
    './attachment_02.xls',
    0,
    first_col=0,
    last_col=None,
    header=True)
lines = apps.sheet_to_array(
    './attachment_02.xls',
    1,
    first_col=0,
    last_col=1,
    header=True)
lines = lines.astype(int)
police = apps.sheet_to_array(
    './attachment_02.xls',
    2,
    first_col=0,
    last_col=None,
    header=True)
inoutCity = apps.sheet_to_array(
    './attachment_02.xls',
    3,
    first_col=1,
    last_col=1,
    header=True)

inoutA = apps.sheet_to_array(
    './attachment_02.xls',
    3,
    first_col=2,
    last_col=2,
    header=True)

base = apps.sheet_to_array(
    './attachment_02.xls',
    4,
    first_col=0,
    last_col=None,
    header=True)
