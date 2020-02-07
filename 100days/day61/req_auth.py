"""
在访问网站时，我们经常会遇到需要身份认证的页面，需要输入用户名和密码才能登录网站。这个时候我们可以使用 Requests 自带的身份认证功能。
"""

import requests

from requests.auth import HTTPBasicAuth

resp = requests.get('http://www.baidu.com', auth=HTTPBasicAuth('username','password'))
print(resp.status_code)