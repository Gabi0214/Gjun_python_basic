import speech_recognition as sr

def generate_subtitles(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # 讀取音訊檔案

    try:
        # 使用Google Speech Recognition API辨識音訊
        text = recognizer.recognize_google(audio_data, language='zh-TW')
        return text
    except sr.UnknownValueError:
        print("無法辨識音訊")
        return ""
    except sr.RequestError as e:
        print(f"Google Speech Recognition API 錯誤： {e}")
        return ""

if __name__ == "__main__":
     # 替換為實際的音訊檔案路徑
    audio_file_path = r"C:\Users\閻佳章\Downloads\cn52000_7311285702925356293.mp4"

    subtitles = generate_subtitles(audio_file_path)

    if subtitles:
        print("自動生成字幕：")
        print(subtitles)
    else:
        print("未能生成字幕。")
