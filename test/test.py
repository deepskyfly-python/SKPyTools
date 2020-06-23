import os
import traceback
import requests
import hashlib
from pyquery import PyQuery as pq

testStr = '000.wav'
print(testStr.split('.')[0])

testStr2 = 'word = %s = %d' % ('sky',1)
print(testStr2)


# md5 sha1
m = hashlib.md5()
testStr = 'essential'.encode(encoding='utf8')
m.update(testStr)
print(m.hexdigest())
print(hashlib.sha1(testStr).hexdigest())


# path
# print("获取当前文件路径——" + os.path.realpath(__file__))  # 获取当前文件路径

# parent = os.path.dirname(os.path.realpath(__file__))
# print("获取其父目录——" + parent)  # 从当前文件路径中获取目录

# garder = os.path.dirname(parent)
# print("获取父目录的父目录——" + garder)
# print("获取文件名" + os.path.basename(os.path.realpath(__file__)))  # 获取文件名

# # 当前文件的路径
# pwd = os.getcwd()               
# print("当前运行文件路径" + pwd)

# # 当前文件的父路径
# father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
# print("运行文件父路径" + father_path)

# # 当前文件的前两级目录
# grader_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
# print("运行文件父路径的父路径" + grader_father)

import re
instr = '正确的句子:[answer]Regular exercise can increase one’s self-confidence[/answer] 正确的句子:[answer]ssssss[/answer]'
regStr = r'\[answer\]([^\[]*)\[/answer\]'
print(re.match(regStr,instr))
print(re.search(regStr,instr).group())
print(re.findall(regStr,instr))
print(re.findall(r'\[answer\](?:[^\[]*)\[/answer\]',instr))