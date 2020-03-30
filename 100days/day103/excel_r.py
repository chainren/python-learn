import xlrd

# 打开要读取的excel文件
wb = xlrd.open_workbook('test_w.xls')

# 打印sheet数量
print('sheet count : %s' % wb.nsheets)

# 获取并打印 sheet 名称
print('sheet names : %s' % wb.sheet_names())

# 根据索引获取sheet页，或者根据name获取
sh1 = wb.sheet_by_index(0)
# sh1 = wb.sheet_by_name('成绩')

# 获取并打印该 sheet 行数和列数
print(u"sheet %s 共 %d 行 %d 列" % (sh1.name, sh1.nrows, sh1.ncols))

# 根据坐标获取数据，第一行第二列。索引从0开始
print('row1-col2 : %s' % sh1.cell_value(0, 1))

# 获取第一行整行数据
row1 = sh1.row_values(0)
print('row1: %s' % row1)

# 获取第二列内容
col1 = sh1.col_values(1)
print('col1: %s' % col1)

#获取某个单元格格式
print('row2-col1 type: %s' % sh1.cell(1, 0).ctype)

# 遍历所有表格内容
for sh in wb.sheets():
    for r in range(sh.nrows):
        # 输出每一行
        print(sh.row(r))