from bs4 import BeautifulSoup
import genanki
import re
import sys
from SKGenAnki import SKGenAnki
sys.path.append("..")
from skcom.SKYouDao import SKYouDao

# fileName = '语法改错400句.htm'
# my_deck = genanki.Deck(2059411252,'语法改错400句')

fileName = '100句翻译.htm'
my_deck = genanki.Deck(2059411251,'100句翻译')

# fileName = '100句翻译_扩展.htm'
# my_deck = genanki.Deck(2059411250,'100句翻译_扩展')


def isQuestionParagraph(p):
    if p['class'] == ['MsoListParagraph']:
        return True
    
    if p.has_attr('style') and p['style'].find('mso-list') != -1:
        return True

    return False

def addNewNote(qStr,aStr):
    #print(qStr)
    fileList = []
    text = re.sub(r'(<img.*src=")(.*/)(.*)"',r'\1\3',aStr)

    soup = BeautifulSoup(text,'html.parser')    
    ansStr = SKGenAnki.getTagWord(soup.get_text())    
    myMedia ='[sound:'+SKYouDao.getMd5FileName(ansStr)+'.mp3]'
    audioFile = SKYouDao.getWordAudio(ansStr,useMd5Name=True)
    fileList.append(audioFile)

    text = SKGenAnki.clearTags(text)
    my_deck.add_note(genanki.Note(model=SKGenAnki.WordModelInput,fields=[qStr, ansStr,myMedia,text]))

    return fileList

def main_run():
    soup = BeautifulSoup(open(fileName,encoding='utf-8'),'html.parser')

    qustStr = ''
    answerStr = ''
    my_package = genanki.Package(my_deck)

    pCount = len(soup.findAll('p'))    
    for pp in soup.find_all('p'):
        pCount -= 1
        if isQuestionParagraph(pp):
            if qustStr != '':
                fList = addNewNote(qustStr,answerStr)
                my_package.media_files += fList

            qustStr = pp.prettify()
            answerStr = ''            
        else:
            answerStr += pp.prettify()
            if pCount == 0:
                fList = addNewNote(qustStr,answerStr)
                my_package.media_files += fList
     
     
    for ii in soup.find_all('img'):
        #print(ii['src'])
        my_package.media_files.append(ii['src'])

    my_package.write_to_file(f"{fileName}.apkg")


if __name__ == '__main__':
    main_run()
    # sss = '<img width="553" height="73" src="test.files/image002.png" alt="IMG_256" v:shapes="图片_x0020_8">'
    # print(re.sub(r'(<img.*src=")(.*/)(.*)"',r'\1\3',sss))

