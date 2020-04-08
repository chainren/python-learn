import csv


# reader(csvfile, dialect='excel', **fmtparams)
# 返回一个 reader 对象，该对象将逐行遍历 csvfile，csvfile 可以是文件对象和列表对象，如果是文件对象要使用 newline='' 打开
with open('test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter= ' ')
    for row in reader:
        print(', '.join(row))
