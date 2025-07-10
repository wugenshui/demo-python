import requests

# 配置请求使用的SOCKS代理
proxies = {
    "http": "socks5://192.168.0.30:9529",
    "https": "socks5://192.168.0.30:9529",
}
response = requests.get("https://www.google.com", proxies=proxies)
print(response.text)
