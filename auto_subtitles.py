import speech_recognition as sr
from pydub import AudioSegment
import srt  # 替换为srt库
import io
import os
from datetime import timedelta


def split_audio(audio_file_path, segment_duration=10):
    audio = AudioSegment.from_file(audio_file_path, format="wav")
    segments = []
    for start_time in range(0, len(audio), segment_duration * 1000):
        end_time = min(start_time + segment_duration * 1000, len(audio))
        segment = audio[start_time:end_time]
        segments.append(segment)
    return segments


def generate_subtitles(audio_file_path, output_subtitle_path, segment_duration=10):
    # 将音频文件分割成小段
    audio_segments = split_audio(audio_file_path, segment_duration)

    # 创建一个语音识别器对象
    recognizer = sr.Recognizer()

    # 创建SRT字幕文件对象
    subtitles = []

    # 对每个小段进行语音识别，并添加到字幕文件中
    start_time = timedelta(seconds=0)
    for i, audio_segment in enumerate(audio_segments):
        try:
            # 将 Pydub 的 AudioSegment 保存到本地临时文件
            temp_audio_path = f"temp_audio_{i}.wav"
            audio_segment.export(temp_audio_path, format="wav")

            # 使用Google Web Speech API进行语音识别
            with sr.AudioFile(temp_audio_path) as source:
                audio_data = recognizer.record(source)

            text = recognizer.recognize_google(
                audio_data, language='zh-TW', show_all=False)

            # 获取小段的时长
            duration = len(audio_segment) / 1000

            # 创建SRT字幕项并添加到文件中
            end_time = start_time + timedelta(seconds=duration)
            subtitle_item = srt.Subtitle(
                index=i + 1, start=start_time, end=end_time, content=text)
            subtitles.append(subtitle_item)

            # 更新起始时间
            start_time = end_time

        except sr.UnknownValueError:
            print(f"语音识别未能理解音频内容 (Segment {i + 1})")
        except sr.RequestError as e:
            print(f"无法连接到Google Web Speech API; {e}")
        finally:
            # 删除临时音频文件
            if os.path.exists(temp_audio_path):
                os.remove(temp_audio_path)

    # 保存字幕檔
    with open(output_subtitle_path, "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))
    print("字幕檔生成成功！")


# 指定输入音频文件路径和输出字幕檔路径
audio_file_path = "./ScrambledEggsFriedShrimps-vocals.wav"
output_subtitle_path = "./ScrambledEggsFriedShrimps-vocals.srt"

# 生成字幕檔
generate_subtitles(audio_file_path, output_subtitle_path)
