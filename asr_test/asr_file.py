# -*- coding: utf-8 -*-
# @Time    : 2023/5/16 20:01
# @Author  : chenhaibing01
# @File    : asr_file.py
# @Software: PyCharm
import sounddevice as sd
import soundfile as sf

class SPEECH2FILE:
    def __init__(self):
        self.duration = 5  # 录制时长（秒）
        self.sample_rate = 16000  # 采样率


    def record_audio(self):
        # 录制麦克风音频
        print(f"开始录音，请说话...(时长为{self.duration}秒)")
        audio = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1)
        sd.wait()  # 等待录音完成
        return audio

    def save_audio_to_file(self, audio, file_path):
        sf.write(file_path, audio, self.sample_rate)


if __name__ == "__main__":
    speech2file = SPEECH2FILE()

    # 录制音频
    audio = speech2file.record_audio()

    # 保存音频为文件
    file_path = 'recorded_audio2.wav'
    speech2file.save_audio_to_file(audio, file_path)

    print("录音已保存为文件：", file_path)

