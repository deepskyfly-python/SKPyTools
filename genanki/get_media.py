import os
import traceback
import requests
from pyquery import PyQuery as pq

def get_txt(word):
    api = f"http://dict.kekenet.com/en/{word}"
    try:
        resp = requests.get(api, timeout=10)
        if resp.status_code == 200:
            html = resp.content
            doc = pq(html)
            return doc.find("#s_ul").text().split('\n')
    except:
        print("请求出错!")
        traceback.print_exc()
        return ["无例句", "无例句"]

def get_mp3(word):
    api = f"http://media.shanbay.com/audio/us/{word}.mp3"
    filepath = f"./mp3/{word}.mp3"
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

if __name__ == '__main__':
    get_txt("america")
    