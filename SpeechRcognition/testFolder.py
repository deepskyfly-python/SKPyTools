# -*- coding: utf-8 -*-
import speech_recognition as sr
import os

filePath = 'm3t1'


def getFileNames(file_dir,audioList):
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        audioList +=files

def getAudioText(audioFile):
    print(audioFile)
    r = sr.Recognizer() 
    test = sr.AudioFile(audioFile)
 
    with test as source:
        audio = r.record(source)
 
    type (audio) 

    result = r.recognize_google(audio, language='en-US', show_all= True)
    # result = r.recognize_google(audio, language='zh-CN', show_all= True)

    print(result)
    if len(result) > 0:
        return result['alternative'][0]['transcript']
    else:
        return ''


audioList =[]
getFileNames(filePath,audioList)

print(audioList)

audioMap = {}

for f in audioList:
    if str.find(f,'wav') > 0:        
        speechStr = (getAudioText('./'+filePath+'/'+f))
        if speechStr != '':
            print(speechStr)
            audioMap[f] = speechStr


print(audioMap)
for k,v in audioMap.items():
    try:
        os.rename('./'+filePath+'/'+k,'./'+filePath+'/'+k.split('.')[0]+'_'+v+'.wav')
    except :
        pass
    





