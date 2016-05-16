from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os
import speech_recognition as sr
import wave
import os
import contextlib
import sys
from os import path
path_dir = ""
class ConvertDialog(FloatLayout):
 	convert = ObjectProperty(None)
 	cancel = ObjectProperty(None)

class Root(FloatLayout):
    convertfile = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_convert(self):
     	content = ConvertDialog(convert=self.convert, canscel=self.dismiss_popup)
     	self._popup = Popup(title="Convert file", content=content , size_hint=(0.9, 0.9) )
     	self._popup.open();

    def convert(self,path,filename):
    	path_dir = os.path.join(path, filename[0])
        os.system("python wav_transcribe.py " + path_dir+" > new_file.srt")
    	self.dismiss_popup()
        

class Editor(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('ConvertDialog', cls=ConvertDialog)

if __name__ == '__main__':
    Editor().run()