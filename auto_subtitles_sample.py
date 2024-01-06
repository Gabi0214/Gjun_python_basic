import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import srt
from datetime import timedelta
import tempfile
import os


def split_audio_with_vad(audio_file_path, silence_threshold=-36):
    audio = AudioSegment.from_file(audio_file_path, format="wav")

    # 使用 pydub.silence.split_on_silence 方法進行 VAD 分割
    segments = split_on_silence(audio, silence_thresh=silence_threshold)

    return segments


def generate_subtitles_with_vad(audio_file_path, output_subtitle_path, silence_threshold=-36):
    audio_segments = split_audio_with_vad(audio_file_path, silence_threshold)

    recognizer = sr.Recognizer()
    subtitles = []
    start_time = timedelta(seconds=0)

    for i, audio_segment in enumerate(audio_segments):
        try:
            # 將 Pydub 的 AudioSegment 保存到本地臨時文件
            temp_audio_fd, temp_audio_path = tempfile.mkstemp(suffix=".wav")
            os.close(temp_audio_fd)
            audio_segment.export(temp_audio_path, format="wav")

            with sr.AudioFile(temp_audio_path) as source:
                audio_data = recognizer.record(source)

            text = recognizer.recognize_google(
                audio_data, language='zh-TW', show_all=False)
            duration = len(audio_segment) / 1000

            end_time = start_time + timedelta(seconds=duration)
            subtitle_item = srt.Subtitle(
                index=i + 1, start=start_time, end=end_time, content=text)
            subtitles.append(subtitle_item)

            start_time = end_time

        except sr.UnknownValueError:
            print(f"無法識別音訊內容 (Segment {i + 1})")
        except sr.RequestError as e:
            print(f"無法連接到Google Web Speech API; {e}")
        finally:
            # 刪除臨時音訊文件
            if os.path.exists(temp_audio_path):
                os.remove(temp_audio_path)

    with open(output_subtitle_path, "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))
    print("字幕檔生成成功！")


# 指定輸入音訊文件路徑和輸出字幕檔路徑
audio_file_path = "./ScrambledEggsFriedShrimps-vocals.wav"
output_subtitle_path = "./ScrambledEggsFriedShrimps-vocals.srt"

# 生成字幕檔
generate_subtitles_with_vad(audio_file_path, output_subtitle_path)
