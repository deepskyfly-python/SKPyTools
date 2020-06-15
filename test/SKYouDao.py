import os
import traceback
import requests
from pyquery import PyQuery as pq

str = '000.wav'
print(str.split('.')[0])



def get_mp3(word):
    api = f"http://dict.youdao.com/dictvoice?type=1&audio={word}"
    filepath = f"./{word}.mp3"
    try:
        if not os.path.exists(filepath):
            res = requests.get(api, timeout=5)
            if res.status_code == 200:
                with open(filepath, "wb") as file:
                    file.write(res.content)
                return filepath
            else:
                print("获取失败 可能是单词拼写错误")
        else:
            return filepath
    except:
        print('下载mp3 请求出错')

def get_sentence_mp3(word):
    api = f"http://dict.youdao.com/dictvoice?audio={word}.&le=eng"
    filepath = f"./{word}.mp3"
    try:
        if not os.path.exists(filepath):
            res = requests.get(api, timeout=5)
            if res.status_code == 200:
                with open(filepath, "wb") as file:
                    file.write(res.content)
                return filepath
            else:
                print("获取失败 可能是单词拼写错误")
        else:
            return filepath
    except:
        print('下载mp3 请求出错')


       


get_mp3('sky')
get_sentence_mp3('''in+the+sky''')