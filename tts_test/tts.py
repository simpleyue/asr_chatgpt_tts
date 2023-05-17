# -*- coding: utf-8 -*-
# @Time    : 2023/5/17 12:36
# @Author  : chenhaibing01
# @File    : tts.py
# @Software: PyCharm

from gtts import gTTS
from playsound import playsound
import os

class TTS:

    def __init__(self):
        self.file_path = os.path.dirname(__file__)
        print(self.file_path)



    def tts(self,file_path):
        # 文字转语音
        text = "Hello, how are you?"
        tts = gTTS(text=text, lang='en')  # 指定语言为英语
        tts.save("output.wa")  # 保存语音为 MP3 文件

    # 播放语音
    # playsound("output.mp3")

if __name__ == "__main__":
    tts = TTS()
