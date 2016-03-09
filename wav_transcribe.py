import speech_recognition as sr
from datetime import datetime
startTime = datetime.now()
#for checking the execution time
from os import path
WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")
r = sr.Recognizer()#initializing a recognizer
with sr.WavFile(WAV_FILE) as source:
    audio = r.record(source)#get the waveform from the wav file
try:
    print(r.recognize_google(audio))#prints the recognized words
    print datetime.now() - startTime#prints the execution time
except sr.UnknownValueError:
    print()#throwing an error if the speech is not understandable 
except sr.RequestError as e:
    print(format(e))#throwing error if there is problem with the connection to the api
