# -*- coding:utf-8 -*-

# orm框架 - SQLAlchemy

# 安装：pip install sqlalchemy

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类
Base = declarative_base()

# 定义对象
class User(Base):
    # 表名
    __tablename__ = 'user'

    # 表结构
    id = Column(String(20), primary_key=True)
    mobile = Column(String(32))

# 初始化数据库连接: '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/test')

# 创建DBSession
DBSession = sessionmaker(bind=engine)

#
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='1').one()

print('type:', type(user))
print('mobile:', user.mobile)

session.close()

