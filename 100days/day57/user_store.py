from werkzeug.security import generate_password_hash, check_password_hash
import uuid

from flask_login import UserMixin

USERS = [
    {
        "id": 1,
        "name": 'lily',
        "password": generate_password_hash('123')
    },
    {
        "id": 2,
        "name": 'tom',
        "password": generate_password_hash('123')
    }
]

# 添加用户
def create_user(user_name, password):
    user = {
        'id': uuid.uuid4(),
        'name': user_name,
        'passowrd': generate_password_hash(password)
    }
    USERS.append(user)

# 获取用户
def get_user(user_name):
    for user in USERS:
        if user['name'] == user_name:
            return user
        return None

# 定义登录用户类，继承flask_login.UserMixin
class User(UserMixin):
    def __init__(self, user):
        self.username = user.get('name')
        self.password_hash = user.get('password')
        self.id = user.get('id')
    
    def verify_pwd(self, password):
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return self.id

    @staticmethod
    def get(user_id):
        if not user_id:
            return None
        for user in USERS:
            if user.get('id') == user_id:
                return User(user)
        return None
