from docx import Document
from docx.shared import Inches

#获取文章全部内容
doc=Document('demo.docx')
#一级标题
print('read ==> Heading 1')
for p in doc.paragraphs:
    if p.style.name=='Heading 1':
        print(p.text)
 
 
#二级标题
print('read ==> Heading 2')
for p in doc.paragraphs:
    if p.style.name=='Heading 2':
        print(p.text)
 
 
#所有标题
import re
print('read ==> All Headings')
for p in doc.paragraphs:
    if re.match("^Heading \d+$",p.style.name):
        print(p.text)
 
#所有内容
print('read ==> Normal')
for p in doc.paragraphs:
    if p.style.name=='Normal':
        print(p.text)
#从前面可以看出，如果知道不同内容的style.name，那么要读这些内容是极其方便的，这些style.name可以通过：
#print(p.style.name)得到
 
for p in doc.paragraphs:
   if p.style.name=='级别3：黑体 13磅 20行距 段落前后20 左对齐':
        print(p.text)
        #输出对应内容