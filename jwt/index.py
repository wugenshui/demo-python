import jwt
import datetime

# 密钥，用于签名和验证JWT
secret_key = '1234567890'

# 载荷，即JWT中包含的信息
payload = {
  'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=1),
  'userId': '1',
  'appId': '123456',
  'system': "大模型应用开发及运行平台"
}

# 生成JWT
token = jwt.encode(payload, secret_key, algorithm='HS256')
print('Generated JWT:', token)

# 解析JWT
# 待验证的JWT token
received_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTc0ODYzMTgsInVzZXJJZCI6IjEiLCJhcHBJZCI6IjEyMzQ1NiIsInN5c3RlbSI6IuWkp-aooeWei-W6lOeUqOW8gOWPkeWPiui_kOihjOW5s-WPsCJ9.pWPEW8MfvHqgPQqWtewtcsU0ecDHbnGPir3H-RgJQR4'
try:
    # JWT解码
    decoded_payload = jwt.decode(received_token, secret_key, algorithms=['HS256'])
    print('Decoded Payload:', decoded_payload)
except jwt.ExpiredSignatureError:
    print('JWT has expired.')
except jwt.InvalidTokenError:
    print('Invalid JWT.')
