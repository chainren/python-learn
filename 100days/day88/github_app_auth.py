from flask import Flask, session,render_template,url_for, redirect

from authlib.integrations.flask_client import OAuth, token_update
from authlib.oauth2.rfc6749.wrappers import OAuth2Token

app = Flask(__name__)
app.secret_key = '!secret'

# 用flask应用实例化OAuth
oauth = OAuth(app)


# 认证服务器配置
app.config['GITHUB_CLIENT_ID']='' # 在github上申请app 并获取
app.config['GITHUB_CLIENT_SECRET'] = ''
app.config['GITHUB_AUTHORIZE_URL'] = 'https://github.com/login/oauth/authorize'
app.config["GITHUB_AUTHORIZE_PARAMS"] = {
    'scope': 'user repo'
}
app.config["GITHUB_ACCESS_TOKEN_URL"] = 'https://github.com/login/oauth/access_token'
app.config["GITHUB_API_BASE_URL"] = 'https://api.github.com'


# 认证服务器实例 
# 方法会根据配置创建认证服务器实例，参数同配置中的前缀，大小写随意
github = oauth.register('github')


# 登录，重定向到github认证页面
@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return github.authorize_redirect(redirect_uri)


# 认证回调函数
@app.route('/auth/redirect')
def auth():
    token = github.authorize_access_token()
    print('====================== token = %s' % token)
    user = github.get('user').json()
    """
     可以在此保存 token 和 用户信息，例如存入数据库
    """
    session['user'] = user
    return redirect('/')


# 首页
@app.route('/')
def home():
    user = session.get('user')
    return render_template('home.html', user=user)

# 退出
def logout():
    session.pop('user', None)
    return redirect('/')


# 刷新access_token 
# 需安装blinker ： pip install blinker

@token_update.connect_via(app)
def on_token_update(sender, name, token, refresh_token=None, access_token=None):
    if refresh_token:
        item = OAuth2Token.find(name=name, refresh_token=refresh_token)
    elif access_token:
        item = OAuth2Token.find(name=name, access_token=access_token)
    else:
        return

    # 更新 access_token
    item.access_token = token['access_token']
    item.refresh_token = token.get('refresh_token')
    item.expires_at = token['expires_at']
    item.save()


if __name__ == '__main__':
    app.run(debug=True)
