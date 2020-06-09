import genanki
import xlrd
from get_media import get_txt, get_mp3

my_deck = genanki.Deck(
    2059400110,
    '英语(二) 4500单词')

# anki 的牌model 可以根据自己的想法设置
my_model = genanki.Model(
    1091735104,
    'Simple Model with Media',
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
            'qfmt': '{{Question}}<br>{{MyMedia}}',  # AND THIS
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<hr id="text">{{Text}}',
        },
    ])

def read_xlsx():
    workbook = xlrd.open_workbook("4500.xlsx")
    Words = workbook.sheet_by_name("Sheet1")
    rows = Words.nrows
    word_list  = []

    # 便利了excel中 第一行 所有的单词
    for x in range(0,rows):
        # 对 带有/ 的双词  及 带有 ()的情况做丢弃处理
        word_str = Words.row(x)[0].value.split('(')[0].split('/')[0]

        # 中文释义 是第三列的内容
        answer  = Words.row(x)[2].value

        # 获取例句
        text_list = get_txt(word_str)

        text = ''
        for x in text_list:
            text += "<br>" + x
            
        my_note = genanki.Note(
            model=my_model,
            # 变量传入牌面
            #     fields=[
            #         {'name': 'Question'},
            #         {'name': 'Answer'},
            #         {'name': 'MyMedia'},
            #         {'name': 'Text'}# ADD THIS
            #     ],
            # 依次传入 sound 只要传入该文件名即可 这个是在anki的内部对封装在apkg内的音频调用  不用有本机路径
            fields=[word_str, answer, f'[sound:{word_str}.mp3]', text])

        # 获取音频
        filepath = get_mp3(word_str)
        if filepath:
            # 文件路径的列表
            word_list.append(filepath)

        print(word_str)
        my_deck.add_note(my_note)
        
    print('list:', word_list)
    my_package = genanki.Package(my_deck)

    # 这里才是音频压入apkg的地方 将所有音频文件路径 传入anki
    my_package.media_files = [ x for x in word_list]
    print(my_package.media_files)
    my_package.write_to_file("4500.apkg")

if __name__ == '__main__':
    read_xlsx()