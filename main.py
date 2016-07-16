from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from multiprocessing import Process
import speech_recognition as sr
import wave
import os
import contextlib
import sys
from os import path
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
		pr = Process(target=function, args=(path_dir, "new_file.srt"))
		print path_dir
		pr.start()
		pr.join()
		self.dismiss_popup()
        

class Editor(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('ConvertDialog', cls=ConvertDialog)

def function(path_dir, ext_file):
    i = 0
    
    WAV_FILE = path.join(ext_file)
    extension = ""
    extension = WAV_FILE.split(".")[-1]
    if (extension != "wav"):
        os.system("avconv -i " + WAV_FILE + "  -vn -f wav temp.wav")
        WAV_FILE  = "temp.wav"
    fname = WAV_FILE
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        end = duration
    r = sr.Recognizer()
    start = 0.0;
    end_time = 4.0;
    while(start != end):
        i+=1
        with sr.WavFile(WAV_FILE) as source:
            audio = r.record(source,end_time, start)
            start += 4.0
            end_time += 4.0
        try:
            print '\n', i,'\n',start," --> ",end_time , r.recognize_google(audio),
        except sr.UnknownValueError:
            print "",
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        os.remove("temp.wav")
    return 0


if __name__ == '__main__':
    Editor().run()