"""
代理设置
"""

import requests

proxies = {
    'http': 'http://127.0.0.1:9001',
    'https': 'https://127.0.0.2:9002'
}

resp = requests.get('http://www.baidu.com', proxies=proxies)