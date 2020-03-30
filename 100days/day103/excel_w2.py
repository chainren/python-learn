import xlwt

# 设置写出格式字体红色加粗
styleBR = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')

# 设置数字型格式为小数点后保留两位
styleNum = xlwt.easyxf(num_format_str='#,##0.00')

# 设置日期型格式显示为YYYY-MM-DD
styleDate = xlwt.easyxf(num_format_str='YYYY-MM-DD')

wb = xlwt.Workbook()

sh1 = wb.add_sheet('成绩')
sh2 = wb.add_sheet('汇总')

# 然后按照位置来添加数据,第一个参数是行，第二个参数是列
sh1.write(0, 0, '姓名', styleBR)   # 设置表头字体为红色加粗
sh1.write(0, 1, '日期', styleBR)   # 设置表头字体为红色加粗
sh1.write(0, 2, '成绩', styleBR)   # 设置表头字体为红色加粗

# 插入数据
sh1.write(1, 0, '张三',)
sh1.write(1, 1, '2019-01-01', styleDate)
sh1.write(1, 2, 88, styleNum)
sh1.write(2, 0, '李四')
sh1.write(2, 1, '2019-02-02')
sh1.write(2, 2, 99.5, styleNum)

# 设置单元格内容居中的格式
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
style = xlwt.XFStyle()
style.alignment = alignment

# 合并A4,B4单元格，并将内容设置为居中
sh1.write_merge(3, 3, 0, 1, '总分', style)

# 使用公式，计算c2+c3单元格的和
sh1.write(3, 2, xlwt.Formula('c2+c3'))

sh2.write(0, 0, '总分', styleBR)
sh2.write(1, 0 , 187.5)

wb.save('test_w2.xls')