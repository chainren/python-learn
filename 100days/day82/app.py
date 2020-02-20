from flask import Flask

from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


# User类，用于模拟用户实体

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def __str__(self):
        return "User(id='%s')" % self.id

# 
users = [
    User(1,'user1', '123456'),
    User(2,'user2', '123456'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

# 获取认证的回调函数，从 request 中得到登录凭证，返回凭证所代表的 用户实体
def authenticate(username, password):
    user = userid_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user
    

# 通过 token 获得认证主体的回调函数
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
# 用 JWT 初始化应用
jwt = JWT(app, authenticate, identity)


@app.route('/protected', methods=['GET','POST'])
@jwt_required() # 声明需要 token 才能访问
def protected():
    # 验证通过返回 认证主体
    return '%s' % current_identity 


if __name__=='__main__':
    app.run(debug=True)