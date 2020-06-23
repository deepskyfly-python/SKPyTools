import os
import re
import sys
import traceback
import requests
import hashlib
import xlrd
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

class SKYouDao:
    api_word_uri = "http://dict.youdao.com/w/"

    @staticmethod
    def getMd5FileName(word):
        return hashlib.md5(word.encode(encoding='utf-8')).hexdigest()

    @staticmethod
    def getWordAudio(word,savePath='./_audioFiles/',useMd5Name=False):
        if not os.path.exists(savePath):
            os.mkdir(savePath)
        filepath = f"{savePath}/{word}.mp3"
        if useMd5Name:
            md5Name = SKYouDao.getMd5FileName(word)
            filepath = f"{savePath}/{md5Name}.mp3"

        rpWord = re.sub(r'\s+','+',word)
        # type=0 us ,type=1 en
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
    def getWordAudio2(word,savePath='./_audioFiles/',useMd5Name=False):
        if not os.path.exists(savePath):
            os.mkdir(savePath)

        filepath = f"{savePath}/{word}.mp3"
        if useMd5Name:
            md5Name = md5Name = SKYouDao.getMd5FileName(word)
            filepath = f"{savePath}/{md5Name}.mp3"
        rpWord = re.sub(r'\s+','+',word)
        api = f"http://dict.youdao.com/dictvoice?audio={rpWord}&le=eng&type=0"
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
    def getWordVideo(word):
        print(os.path.split(os.path.realpath(__file__))[0]+"/wordVideos.xls")
        workbook = xlrd.open_workbook(os.path.split(os.path.realpath(__file__))[0]+"/wordVideos.xls")
        sheet = workbook.sheet_by_name("word")
        nrows = sheet.nrows
        for i in range(nrows):
            # print(sheet.row(i))
            if sheet.row(i)[0].value == word:
                # print(word)
                return sheet.row(i)[1].value
        
        return ''
        

    @staticmethod
    def getWordAnkiCard(word,savePath='./_audioFiles/'):
        if not os.path.exists(savePath):
            os.mkdir(savePath)
        url = SKYouDao.api_word_uri + str.replace(word,' ','%20')
        requestFile = requests.get(url, timeout=10)
        soup = BeautifulSoup(requestFile.content,'html.parser')

        outStr = '<br/>'
        urlStr = f'>>[<a href="{url}" >YouDao</a>]'
        baiduUrl = 'https://fanyi.baidu.com/#en/zh/'+word
        urlStr += f'>>[<a href="{baiduUrl}" >Baidu</a>]'
        
        wordVideo = SKYouDao.getWordVideo(word)
        if wordVideo != '':
            urlStr += f'>>[<a href="{wordVideo}" >WordVideo</a>]'

        print(urlStr)

        phrsListTab = ''
        tEETrans = ''
        bilingual = ''
        try:
            phrsListTab = soup.find('div',id='phrsListTab').prettify()
            tEETrans = soup.find('div',id='tEETrans').prettify()
        except :
            pass        
        
        listFiles = []
        try:
            bilingualObj = soup.find('div',id='bilingual')
            for li in (bilingualObj.ul.find_all('li')):
                # print(li.a)
                wordText = li.a['data-rel'].replace('&le=eng','')
                wordText = wordText.replace('+',' ')
                # print(wordText)
                audioFile = SKYouDao.getWordAudio(wordText,useMd5Name=True)

                new_li_tag = soup.new_tag("li")
                new_li_tag.append('[sound:'+SKYouDao.getMd5FileName(wordText)+'.mp3]')
                li.a.insert_after(new_li_tag)
                print(audioFile)
                if audioFile != None:
                    listFiles.append(audioFile)
                else :
                    print(wordText)

            bilingual = bilingualObj.prettify()
            # print(bilingualObj.ul.li)
            # print(bilingualObj.find_all(attrs={'class':"sp dictvoice voice-js log-js"}))
        except:
            pass

        print(listFiles)
        
        outStr = urlStr + bilingual + phrsListTab + tEETrans
        return outStr,listFiles


       
if __name__ == '__main__':
    # print(SKYouDao.getWordAudio('sky',useMd5Name=True))

    # textSp = '''Sometimes, although it is difficult to evaluate the environmental cost of human activities, there is a necessity for the government enacting legislations to restrict some behaviors , which can also arise people's concern about environmental degradation. '''
    # print(SKYouDao.getWordAudio2(textSp))
    
    (SKYouDao.getWordAnkiCard('husband'))
    