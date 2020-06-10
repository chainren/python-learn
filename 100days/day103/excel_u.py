"""
使用xlutils工具
"""

import xlutils

import xlrd
from xlutils.copy import copy

wb = xlrd.open_workbook('test_w.xls')

# 复制一份
wb = copy(wb)


sh1 = wb.get_sheet(0)

sh1.write(3, 0, '王五')
sh1.write(3, 1, '59')

sh2 = wb.get_sheet(1)

sh1.write(1, 0, 246.5)

wb.save('test_w1.xls')