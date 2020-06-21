from bs4 import BeautifulSoup
import genanki
import re
import sys
import os
sys.path.append("..")
from skcom import SKYouDao

audioPath = './m3t1/'
suffix = 'wav'
fileName = 'WangLu_m3t1'
my_deck = genanki.Deck(1111000010,fileName)


# anki 的牌model 可以根据自己的想法设置
my_model = genanki.Model(
    1111100010, 
    'Word Model Input',
    # 这里是传入fields 的变量代名
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'MyMedia'},
        {'name': 'Text'}# ADD THIS
    ],
    # 直接将你传入的 变量 通过代名 写入模版 html还是很好理解的
    templates=[
        {
            'name': 'Card 1',
            # 'qfmt': '{{Question}}<br>{{MyMedia}}',  # AND THIS
            #  'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<hr id="text">{{Text}}',
            'qfmt': '{{MyMedia}} {{type:Question}}',  # AND THIS
            'afmt': '{{FrontSide}}<hr id="answer">{{type:Question}}{{MyMedia}}{{Answer}}<hr id="text">{{Text}}',
        },
    ],
    css = r'''
.card {
    font-family: arial;
    font-size: 20px;
    text-align: left;
    color: #D1D1D1;
    background-color: #282828;
}
a{color:#C1C1C1 }
.typeGood {color:#33aa33 ; background-color: #003300; }
.typeBad { color:#aa3333;background-color: #330000; }
.typeMissed { background-color: #000000; }
    '''
    )


def addNewNote(qStr,aStr,mediaStr,textStr):
    my_deck.add_note(genanki.Note(model=my_model,fields=[qStr, aStr,mediaStr,textStr]))

def addWordNote(word):
    print(word)
    qustStr = word
    answerStr = word
    mediaFile = word+'.'+suffix
    media = f'[sound:{mediaFile}]'
    # print(media)
    text,audioFiles = SKYouDao.SKYouDao.getWordAnkiCard(word)
    # print(text)
    addNewNote(qustStr,answerStr,media,text)
    return audioFiles

def renameFile():
    files = []
    for root, dirs, files in os.walk(audioPath):
        pass

    for f in files:
        try:
            os.rename(audioPath+f,audioPath+f.split('_')[1])
        except :
            pass


def main_run():
    files = []
    for root, dirs, files in os.walk(audioPath):
        pass


    # 
    my_package = genanki.Package(my_deck)
    for f in files:
        word = f.split('.')[0]
        audioFiles = addWordNote(word)
        my_package.media_files += audioFiles

    for f in files:
        print(audioPath+f)
        my_package.media_files.append(audioPath+f)

    my_package.write_to_file(f"{fileName}.apkg")


if __name__ == '__main__':
    renameFile()
    main_run()
    # sss = '<img width="553" height="73" src="test.files/image002.png" alt="IMG_256" v:shapes="图片_x0020_8">'
    # print(re.sub(r'(<img.*src=")(.*/)(.*)"',r'\1\3',sss))

