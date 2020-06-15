from docx import Document

fileName = '语法改错400句'

doc = Document(fileName + '.docx')

# 有中文吗
def check_contain_chinese(check_str):
    # for ch in check_str.decode('utf-8'):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

#每一段的内容
print('#每一段的内容')
count = 0
for para in doc.paragraphs:
    print(para.style.name +": "+ para.text)
    if check_contain_chinese(para.text) == False and len(para.text)>2:
        para.style = 'List Paragraph'
        print(para.style.name +": "+ para.text)
        count +=1


print(f'count = {count}')

doc.save(fileName+'_2.docx')