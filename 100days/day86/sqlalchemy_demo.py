"""
1. 安装 pip install sqlalchemy
"""
import sqlalchemy
from sqlalchemy import create_engine
import pymysql

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker


# 创建映射基类
Base = declarative_base()


print(sqlalchemy.__version__)


class User(Base):
    # 指定表明
    __tablename__='user1'
    # 指定id
    id = Column(Integer, primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    age = Column(Integer)
    sex = Column(String(2))
    income = Column(Float)

# 创建engine

## sqllite
engine = create_engine('sqlite:///foo.db', echo=True)

# mysql
# 添加此行代码，解决找不到Mysqldb 模块的问题
# pymysql.install_as_MySQLdb()

# engine = create_engine('mysql://develop:xs_dev@192.168.160.33/test',
#         echo=True,
#         pool_size=10,
#         pool_recycle=3600)

# conn = engine.connect()
# print(conn)


# 创建表
# Base.metadata.create_all(engine)

# 建立会话
Session = sessionmaker(bind=engine)
# 创建Session实例
session = Session()
# print(session)

# 新增数据
# user1 = User(id=1, first_name='Jhon', last_name='jhon', age=34, sex='M', income=10000)
# 保存
# session.add(user1)
# 提交
# session.commit()
# 关闭
# session.close()

# 查询，如果数据为空，会抛异常 NoResultFound
user2 = session.query(User).filter(User.id==1).one()
print(user2.id, user2.first_name)
print('====================')
# 查询所有数据
users = session.query(User).all()
print(type(users))
for u in users:
    print(u.id, u.first_name)

# 修改
# user3 = session.query(User).filter(User.id==1).one()
# print('修改前first_name=%s' % user3.first_name)
# user3.first_name='Joy'
# session.commit()
# print('修改后first_name=%s' % user3.first_name)

# 删除
# user4 = session.query(User).filter(User.id==1).one()
# session.delete(user4)
# session.commit()
