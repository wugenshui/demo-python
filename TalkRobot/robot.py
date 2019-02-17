import speech_recognition as sr

# 指定要转换的音频源文件（english.wav）
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")

# 定义SpeechRecognition对象并获取音频源文件（english.wav）中的数据
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# 使用CMU Sphinx引擎去识别音频
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# 使用Microsoft Bing Voice Recognition引擎去识别音频
# Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
