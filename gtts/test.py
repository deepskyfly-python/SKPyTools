from gtts import gTTS
import os
import sys
textStr = "regular exercise can increase self-confidence"

# tts = gTTS(text="我们可以一起吃饭吗？",lang="zh-cn")
tts = gTTS(text=textStr)

tts.save(sys.path[0]+"/"+f'{textStr}.mp3')
os.system(sys.path[0]+"/"+f'{textStr}.mp3')