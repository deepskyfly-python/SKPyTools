from bs4 import BeautifulSoup
import genanki
import re
import sys
import os

class SKGenAnki:
    # tags
    answer_tag = ['[answer]','[/answer]']
    sound_tag = ['[sound]','[/sound]']

    # DarkCss
    css_dark = r'''
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

    # anki 的牌model 可以根据自己的想法设置
    SimpleModel = genanki.Model(
        1000500010, 
        'SimpleModel',
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
        css = css_dark
    )

    # anki 的牌model 可以根据自己的想法设置
    SimpleModelInput = genanki.Model(
        1000500011, 
        'SimpleModelInput',
        # 这里是传入fields 的变量代名
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
            {'name': 'Text'}
        ],
        # 直接将你传入的 变量 通过代名 写入模版 html还是很好理解的
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}{{type:Answer}}',  # AND THIS
                'afmt': '{{FrontSide}}<hr id="answer">{{type:Answer}}{{Text}}',
            },
        ],
        css = css_dark
    )

    # anki 的牌model 可以根据自己的想法设置
    WordModelInput = genanki.Model(
        1000500020, 
        'WordModelInput',
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
                'qfmt': '{{Question}} {{type:Answer}}',  # AND THIS
                'afmt': '{{FrontSide}}<hr id="answer">{{type:Answer}}{{MyMedia}}{{Answer}}<hr id="text">{{Text}}',
            },
        ],
        css = css_dark
    )

    # anki 的牌model 可以根据自己的想法设置
    WordModelInput2 = genanki.Model(
        1000500021, 
        'WordModelInput',
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
                'qfmt': '{{MyMedia}} {{type:Question}}',  # AND THIS
                'afmt': '{{FrontSide}}<hr id="answer">{{type:Question}}{{MyMedia}}{{Answer}}<hr id="text">{{Text}}',
            },
        ],
        css = css_dark
    )

    @staticmethod
    def convertNoRegular(inStr):
        return inStr.replace('[',r'\[').replace(']',r'\]')

    @staticmethod
    def getTagWord(inStr,tagList=answer_tag):
        print('===>SKGenAnki  GetTagWord')
        # print(inStr)
        # print(tagList)
        searchList = [SKGenAnki.convertNoRegular(tagList[0]),SKGenAnki.convertNoRegular(tagList[1])]
        rs = re.findall(searchList[0]+r'([^\[]*)'+searchList[1],inStr)

        if rs is not None and len(rs) > 0:
            # replace
            # print(rs)
            rs[0] = re.sub(r'\n',' ',rs[0]).strip()
            rs[0] = re.sub(r'\s+',' ',rs[0])
            rs[0] = re.sub('’',"'",rs[0])
            print(rs)
            return rs[0]
        else:
            return ''

        
    @staticmethod
    def clearTags(text):
        return text.replace(SKGenAnki.answer_tag[0],'').replace(SKGenAnki.answer_tag[1],'').replace(SKGenAnki.sound_tag[0],'').replace(SKGenAnki.sound_tag[1],'')

