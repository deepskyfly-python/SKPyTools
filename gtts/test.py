from gtts import gTTS
import os

textStr = "regular exercise can increase self-confidence"

# tts = gTTS(text="我们可以一起吃饭吗？",lang="zh-cn")
tts = gTTS(text=textStr)

tts.save(f'{textStr}.mp3')
os.system(f'{textStr}.mp3')