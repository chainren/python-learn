import csv 


"""
DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)

创建一个对象，该对象在操作上类似常规 writer，但会将字典映射到输出行，fieldnames 参数是由键组成的序列，
它指定字典中值的顺序，这些值会按指定顺序传递给 writerow() 方法并写入文件；如果字典缺少 fieldnames 中的键，
则可选参数 restval 用于指定要写入的值；如果传递给 writerow() 方法的字典的某些键在 fieldnames 中找不到，
则可选参数 extrasaction 用于指定要执行的操作，如果将其设置为默认值 'raise'，则会引发 ValueError， 
如果将其设置为 'ignore'，则字典中的其他键值将被忽略；所有其他可选或关键字参数都传递给底层的 writer 实例
"""

with open('test.csv', 'w', newline='') as csvfile:
    # 定义标题行
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    # 写入字典
    writer.writerow({'id': '1001', 'name': '张三', 'age': '21'})
    writer.writerow({'id': '1002', 'name': '李四', 'age': '31'})

with open('test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter= ' ')
    for row in reader:
        print(', '.join(row))
