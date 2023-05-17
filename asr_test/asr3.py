import speech_recognition as sr

class CATT():

    def convert_audio_to_text(self, file_path):
        r = sr.Recognizer()

        with sr.AudioFile(file_path) as source:
            audio_data = r.record(source)  # 从音频文件中读取音频数据
            # print(str(audio_data))
        while True:
            try:
                text = r.recognize_google(audio_data, language='zh-CN')
                return text
            except sr.UnknownValueError:
                print("语音识别无法理解音频内容")
            except sr.RequestError as e:
                print("无法连接到语音识别服务：{0}".format(e))

        return ""
if __name__ == "__main__":

    catt = CATT()
    # 指定音频文件路径
    file_path = '../recordFile/recorded_audio.wav'

    # 将音频文件转换为文字
    text = catt.convert_audio_to_text(file_path)

    print("转换结果：", text)
