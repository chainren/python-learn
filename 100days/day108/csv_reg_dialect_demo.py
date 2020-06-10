import csv


# 注册方言,所有字段使用"|"分隔
csv.register_dialect('mydialect', delimiter='|', quoting=csv.QUOTE_ALL)

with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, 'mydialect')
    writer.writerow(['id','name','age'])
    writer.writerow(['1001', '张三', 100])

with open('test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter= ' ')
    for row in reader:
        print(', '.join(row))

