import csv

# csvfile 可以是具有 write() 方法的任何对象，如果 csvfile 是文件对象，则使用 newline='' 打开
with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    # writer.writerow(['1001', '张三', '222'])
    # 写入多行
    data = [('1001', '张三', '21'), ('1002', '李四', '31')]
    writer.writerows(data)


