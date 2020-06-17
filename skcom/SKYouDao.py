import os
import re
import traceback
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

class SKYouDao:
    audioDir = "./_audios"
    api_word_uri = "http://dict.youdao.com/w/"

    @staticmethod
    def getWordAudio(word):
        filepath = f"{SKYouDao.audioDir}/{word}.mp3"
        rpWord = re.sub(r'\s+','+',word)
        api = f"http://dict.youdao.com/dictvoice?type=1&audio={rpWord}"
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
            print('下载mp3 请求出错：'+filepath)

    @staticmethod
    def getWordAudio2(word):
        filepath = f"{SKYouDao.audioDir}/{word}.mp3"
        rpWord = re.sub(r'\s+','+',word)
        api = f"http://dict.youdao.com/dictvoice?audio={rpWord}.&le=eng"
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
            print('下载mp3 请求出错：'+filepath)

    @staticmethod
    def getWordAnkiCard(word):
        url = SKYouDao.api_word_uri + str.replace(word,' ','%20')
        requestFile = requests.get(url, timeout=10)
        soup = BeautifulSoup(requestFile.content,'html.parser')

        outStr = '<br/>'
        outStr += f'>>[<a href="{url}" >YouDao</a>]'
        try:
            outStr += soup.find('div',id='phrsListTab').prettify()
            outStr += soup.find('div',id='tEETrans').prettify()
            outStr += soup.find('div',id='bilingual').prettify()       
        except :
            pass
        
        

        return outStr


       
if __name__ == '__main__':
    # if not os.path.exists(SKYouDao.audioDir):
    #     os.mkdir(SKYouDao.audioDir)
    # print(SKYouDao.getWordAudio('sky'))
    # print(SKYouDao.getWordAudio2('''in  the  sky's home'''))
    print(SKYouDao.getWordAnkiCard('sky'))
    