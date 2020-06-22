import os
import re
import traceback
import requests
import hashlib
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq


class SKBaiduFanYi:
    word_api = 'https://fanyi.baidu.com/#en/zh/'

    @staticmethod
    def GetWordURL(word):
        api = SKBaiduFanYi.word_api + word
        return api

    @staticmethod
    def HasWordExplainVideo(word):
        api = SKBaiduFanYi.word_api + word        
        try:
            res = requests.get(api, timeout=20)
            if res.status_code == 200:
                soup = BeautifulSoup(res.content,'html.parser')        
                # print(soup.prettify())     
                wordDiv = soup.find('div', attrs={'class':"trans-left"})  
                print(wordDiv.prettify())
            else:
                print("获取失败 可能是单词拼写错误")
           
        except:
            print('下载mp3 请求出错：')



if __name__ == '__main__':
    SKBaiduFanYi.HasWordExplainVideo('essential')