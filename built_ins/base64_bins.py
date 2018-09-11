# -- coding: utf-8 --

# base64

import base64

encode = base64.b64encode(b'binary\x00string')
print(encode)
decode = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(decode)

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd--__'))


# 练习：写一个能处理去掉=的base64解码函数
def safe_base64_decode(s):
    print(s)
    print(len(s) % 4)
    if len(s) % 4 != 0:
        n = 4 - len(s) % 4;
        print(n)
        s = s + b'=' * n
        print(s)
    return base64.b64decode(s)


if __name__ == '__main__':
    s = safe_base64_decode(b'YWJjZA')
    print(s)
