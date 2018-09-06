# 练习：利用urllib读取JSON，然后将JSON解析为Python对象：


from urllib import request
import json


def fetch_data(url):
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1')
    with request.urlopen(req) as f:
        print('Status: ', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s : %s' % (k, v))
        da = f.read().decode('UTF-8')
        # print('Data: ', da)
        return eval(da)


s = fetch_data('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(s)


