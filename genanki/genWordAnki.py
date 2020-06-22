from bs4 import BeautifulSoup
import genanki
import re
import sys
import os
sys.path.append("..")
from skcom import SKYouDao
from SKGenAnki import SKGenAnki

audioPath = './m3t1/'
suffix = 'wav'
fileName = 'WangLu_m3t1'
my_deck = genanki.Deck(1111000010,fileName)


def addNewNote(qStr,aStr,mediaStr,textStr):
    my_deck.add_note(genanki.Note(model=SKGenAnki.WordModelInput,fields=[qStr, aStr,mediaStr,textStr]))

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

