# -*- coding: utf-8 -*-
# @Time    : 2023/5/17 10:52
# @Author  : chenhaibing01
# @File    : main.py
# @Software: PyCharm

from chatgpt.mulconversation import ChatGPT
from asr_test.asr_file import SPEECH2FILE
from asr_test.asr3 import CATT
import re
import pyttsx3


"""将录音保存为文件"""
file_path = 'recordFile/recorded_audio.wav'
speech2file = SPEECH2FILE()

# 录制音频, 保存音频为文件
audio = speech2file.record_audio()
speech2file.save_audio_to_file(audio, file_path)

# print("录音已保存为文件：", file_path)

print("聆听结束，正在努力搜索答案，不要着急呦...")

"""将录音转换为文字"""
catt = CATT()
text = catt.convert_audio_to_text(file_path)

print("转换结果：", text)

"""将文字作为chatgpt传参"""
text = '这里的天气'
cg = ChatGPT()
conversation = cg.ask(1, text)  # （问题id, 问题）如果是连续的问题，就用相同的问题id
cg.show_conversation(conversation)

speech_text = conversation[-1]["content"]


speech_text = re.sub(r'\n','', speech_text)

"""播放"""

# 创建 TTS 引擎
engine = pyttsx3.init()

# 设置语音参数
engine.setProperty('rate', 150)  # 语速
engine.setProperty('volume', 0.5)  # 音量

# 文字转语音
engine.say(speech_text)

# 播放语音
engine.runAndWait()






