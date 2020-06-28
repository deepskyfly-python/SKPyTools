# -*- coding: utf-8 -*-
import speech_recognition as sr
import os

filePath = 'outputFiles'


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

    result = {}
    try:        
        result = r.recognize_google(audio, language='en-US', show_all= True)
        # result = r.recognize_google(audio, language='zh-CN', show_all= True)
    except :
        print('recognize_google  error!')
        pass

    print(result)
    if len(result) > 0:
        return result['alternative'][0]['transcript']
    else:
        return ''

def renameAudioFile(oldFile,newFile):
    os.rename('./'+filePath+'/'+oldFile,'./'+filePath+'/'+oldFile.split('.')[0]+'_'+newFile+'.wav')


audioList =[]
getFileNames(filePath,audioList)

print(audioList)


for f in audioList:
    if str.find(f,'wav') > 0:        
        speechStr = (getAudioText('./'+filePath+'/'+f))
        if speechStr != '':
            speechStr = speechStr.replace('*','')
            print(speechStr)
            renameAudioFile(f,speechStr)

    





