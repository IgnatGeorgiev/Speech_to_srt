import speech_recognition as sr
from datetime import datetime
startTime = datetime.now()
from os import path
WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "output_audio.wav")
r = sr.Recognizer()
with sr.WavFile(WAV_FILE) as source:
    audio = r.record(source)
try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    print datetime.now() - startTime
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
