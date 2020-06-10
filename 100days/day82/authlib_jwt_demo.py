from authlib.jose import jwt

header = {'alg':'HS256'}
pyload = {
    'iss':'Authlib',
    'sub':'123',
    'name':'bob'
}
secret = '123abc.'

# 生成token
token = jwt.encode(header, pyload, secret)
print(token)

# 解码token
claims = jwt.decode(token, secret)
print(claims)

# header
print(claims.header)

#校验token有效性
print(claims.validate())
