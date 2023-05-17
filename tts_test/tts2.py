# -*- coding: utf-8 -*-
# @Time    : 2023/5/17 13:01
# @Author  : chenhaibing01
# @File    : tts2.py
# @Software: PyCharm

import pyttsx3

# 创建 TTS 引擎
engine = pyttsx3.init(driverName='nsss')

# 设置语音参数
engine.setProperty('rate', 150)  # 语速
engine.setProperty('volume', 0.5)  # 音量

# 文字转语音
text = "你好，我是小度度嘟嘟的对的语音助手"
print(11111,text)
engine.say(text)

# 播放语音
engine.runAndWait()

