import csv 


"""
DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)

创建一个对象，该对象在操作上类似于常规 reader，但是将每行中的信息映射到一个 dict，该 dict 的键由 fieldnames（是一个序列）可选参数给出，
如果省略 fieldnames，则文件第一行中的值将用作字段名；如果某一行中的字段多于字段名，则其余字段将放入列表中，字段名由 restkey 指定（默认为 None），
如果非空白行的字段少于字段名，则缺少的值将用 None 填充。
"""
with open('test.csv', 'w', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['id'], row['name'], row['age'])
    
