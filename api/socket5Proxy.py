# 安装依赖：pip install pysocks
import socks
import socket

# 配置默认的SOCKS代理
host = "192.168.0.30"
port = 9529

socks.set_default_proxy(socks.SOCKS5, host, port, True)
socket.socket = socks.socksocket
print(f"全局代理设置成功，当前代理为:{host}:{port}")

# 现在，所有的网络操作将使用配置的SOCKS代理
# 例如，您可以使用requests库与SOCKS代理进行如下操作：
import requests

response = requests.get("https://www.google.com")
print(response.text)

# 在完成后不要忘记关闭代理
socks.setdefaultproxy()
print("全局代理已关闭")
