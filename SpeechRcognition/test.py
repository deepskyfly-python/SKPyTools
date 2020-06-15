import speech_recognition as sr
 
r = sr.Recognizer()
 
test = sr.AudioFile('test.wav')
 
with test as source:
    audio = r.record(source)
 
type (audio)
 
# print(r.recognize_google(audio, language='zh-CN', show_all= True))

print(r.recognize_google(audio, language='en-US', show_all= True))
