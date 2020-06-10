from bs4 import BeautifulSoup
import genanki
import re

fileName = 'test.htm'
my_deck = genanki.Deck(
    2059411250,
    'test')


# anki 的牌model 可以根据自己的想法设置
my_model = genanki.Model(
    1091735104,
    'Simple Model',
    # 这里是传入fields 的变量代名
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'}
    ],
    # 直接将你传入的 变量 通过代名 写入模版 html还是很好理解的
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',  # AND THIS
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
    css = r'''.card {
    font-family: arial;
    font-size: 20px;
    text-align: left;
    color: black;
    background-color: white;
    }
    '''
    )

def addNewNote(qStr,aStr):
    # print(qustStr)
    aStr = re.sub(r'(<img.*src=")(.*/)(.*)"',r'\1\3',aStr)
    my_deck.add_note(genanki.Note(model=my_model,fields=[qStr, aStr]))

def main_run():
    soup = BeautifulSoup(open(fileName),'html.parser')

    qustStr = ''
    answerStr = ''
    pCount = len(soup.findAll('p'))    
    for pp in soup.find_all('p'):
        pCount -= 1
        if pp['class'] == ['MsoListParagraph']:
            if qustStr != '':
                addNewNote(qustStr,answerStr)

            qustStr = pp.prettify()
            answerStr = ''            
        else:
            answerStr += pp.prettify()
            if pCount == 0:
                addNewNote(qustStr,answerStr)

    my_package = genanki.Package(my_deck)
    for ii in soup.find_all('img'):
        #print(ii['src'])
        my_package.media_files.append(ii['src'])

    my_package.write_to_file(f"{fileName}.apkg")


if __name__ == '__main__':
    main_run()
    # sss = '<img width="553" height="73" src="test.files/image002.png" alt="IMG_256" v:shapes="图片_x0020_8">'
    # print(re.sub(r'(<img.*src=")(.*/)(.*)"',r'\1\3',sss))

