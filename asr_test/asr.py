import sounddevice as sd
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()

    # 录制麦克风音频
    print("开始录音，请说话...")
    duration = 2  # 录制时长（秒）
    sample_rate = 16000  # 采样率
    channels = 1  # 声道数

    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()  # 等待录音完成
    # print(audio.tobytes())
    # a = audio.tobytes()
    # print(a)

    #将音频数据转换为AudioData对象
    audio_data = sr.AudioData(audio.tobytes(), sample_rate, sample_width=4)
    # print(audio_data)
    # 将音频转换为文本
    text = ""
    try:
        text = r.recognize_google(audio_data, language='zh-CN')
    except sr.UnknownValueError:
        print("语音识别无法理解音频内容")
    except sr.RequestError as e:
        print("无法连接到Google Web Speech API： {0}".format(e))

    return text

# 执行语音转文字
text = speech_to_text()
print("转换结果：", text)
