import xlwt

# 创建xls文件
wb = xlwt.Workbook(encoding='utf-8')

# 新增两个表单页
sh1 = wb.add_sheet('成绩')
sh2 = wb.add_sheet('汇总')

# 然后按照位置来添加数据，第一个参数是行，第二个参数是列
# 写入第一个sheet
sh1.write(0, 0, '姓名')
sh1.write(0, 1, '成绩')
sh1.write(1, 0, '张三')
sh1.write(1, 1, 88)
sh1.write(2, 0, '李四')
sh1.write(2, 1, 99.5)

# 写入第二个sheet
sh2.write(0, 0, '总分')
sh2.write(1, 0, 187.5)

# 最后保存文件
wb.save('test_w.xls')