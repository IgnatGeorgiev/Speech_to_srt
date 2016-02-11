#!/usr/bin/env python3

import speech_recognition as test

from os import path
WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")

r = test.Recognizer()
with test.WavFile(WAV_FILE) as source:
    audio = r.record(source) 
try:
    print(r.recognize_google(audio))
except test.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except test.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))