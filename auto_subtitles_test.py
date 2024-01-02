import speech_recognition as sr
import pysrt


def generate_subtitles(audio_file_path, output_subtitle_path):
    # 创建一个语音识别器对象
    recognizer = sr.Recognizer()

    # 使用recognizer的record方法录制音频
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        # 使用Google Web Speech API进行语音识别
        text = recognizer.recognize_google(audio_data, language='zh-TW')

        # 创建SRT字幕文件对象
        subtitles = pysrt.SubRipFile()

        # 将语音识别的文本拆分成多行，并为每行创建一个字幕项
        lines = text.split('\n')
        for i, line in enumerate(lines):
            subtitle_item = pysrt.SubRipItem(
                index=i+1, start=0, end=1000, text=line)
            subtitles.append(subtitle_item)

        # 保存字幕檔
        subtitles.save(output_subtitle_path, encoding='utf-8')

        print("字幕檔生成成功！")
    except sr.UnknownValueError:
        print("语音识别未能理解音频内容")
    except sr.RequestError as e:
        print(f"无法连接到Google Web Speech API; {e}")


# 指定输入音频文件路径和输出字幕檔路径
audio_file_path = "./ScrambledEggsFriedShrimps-vocals.mp3"
output_subtitle_path = "./subtitles.srt"

# 生成字幕檔
generate_subtitles(audio_file_path, output_subtitle_path)
