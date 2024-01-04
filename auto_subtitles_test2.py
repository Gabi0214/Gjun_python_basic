import speech_recognition as sr
from pydub import AudioSegment
import pysrt


def generate_subtitles(audio_file_path, output_subtitle_path):
    # 创建一个语音识别器对象
    recognizer = sr.Recognizer()

    # 使用recognizer的record方法录制音频
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        # 使用Google Web Speech API进行语音识别，获取文本及时间信息
        results = recognizer.recognize_google(
            audio_data, show_all=True, language='zh-TW')

        # 获取语音片段及其对应的时间
        segments = []
        for result in results['alternative']:
            start_time = result['start_time']
            end_time = result['end_time']
            text = result['transcript']
            segments.append({'start_time': start_time,
                            'end_time': end_time, 'text': text})

        # 创建SRT字幕文件对象
        subtitles = pysrt.SubRipFile()

        # 将语音识别的文本及时间信息创建字幕项
        for i, segment in enumerate(segments):
            start_time = int(float(segment['start_time']) * 1000)
            end_time = int(float(segment['end_time']) * 1000)
            subtitle_item = pysrt.SubRipItem(
                index=i + 1, start=start_time, end=end_time, text=segment['text'])
            subtitles.append(subtitle_item)

        # 保存字幕檔
        subtitles.save(output_subtitle_path, encoding='utf-8')

        print("字幕檔生成成功！")
    except sr.UnknownValueError:
        print("语音识别未能理解音频内容")
    except sr.RequestError as e:
        print(f"无法连接到Google Web Speech API; {e}")


# 指定输入音频文件路径和输出字幕檔路径
audio_file_path = "./ScrambledEggsFriedShrimps-vocals.wav"
output_subtitle_path = "./subtitles.srt"

# 生成字幕檔
generate_subtitles(audio_file_path, output_subtitle_path)
