import itchat
import requests


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': 'xxxxxxxxxxxxxx',  # Tuling Key,替换为你自己的
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个 post 请求
    r = requests.post(apiUrl, data=data).json()
    print(r)
    return r.get('text')


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return get_response(msg['Text'])


# @itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
# def print_content(msg):
#     return get_response(msg['Text'])


itchat.auto_login(True)
itchat.run()
