# encoding=utf8

import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key,message, digestmod='MD5')
s = h.hexdigest()
print(s)
