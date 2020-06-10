import genanki

my_deck = genanki.Deck(
    2059411250,
    'test')


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


def main_run():
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
        fields=['word_str', 'answer', 'sound', '''<p class="MsoNormal"><span style="font-family:宋体;color:blue">我的句子：</span><span lang="EN-US" style="color:blue;background:yellow">Excise</span><span style="font-family:宋体;color:blue;background:yellow">动词原形不可以做主语</span><span style="color:blue;background:yellow"> </span><span style="font-family:宋体;
color:blue;background:yellow">要用名词性质的词</span><span lang="EN-US" style="color:
blue;background:yellow"> exercising </span><span lang="EN-US" style="color:blue">&nbsp;regularly
can improve people's self-<span style="background:yellow">confidences
confidence</span></span><span style="font-family:宋体;color:blue;background:yellow">不可数</span></p>'''])

    my_deck.add_note(my_note)
    my_package = genanki.Package(my_deck)
    my_package.write_to_file("4500.apkg")


if __name__ == '__main__':
    main_run()