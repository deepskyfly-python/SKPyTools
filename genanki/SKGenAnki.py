from bs4 import BeautifulSoup
import genanki
import re
import sys
import os

class SKGenAnki:

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
                'qfmt': '{{Question}}',  # AND THIS
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
                'qfmt': '{{MyMedia}} {{type:Question}}',  # AND THIS
                'afmt': '{{FrontSide}}<hr id="answer">{{type:Question}}{{MyMedia}}{{Answer}}<hr id="text">{{Text}}',
            },
        ],
        css = css_dark
    )




