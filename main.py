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




class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


#class SaveDialog(FloatLayout):
 #   save = ObjectProperty(None)
  #  text_input = ObjectProperty(None)
   # cancel = ObjectProperty(None)

class ConvertDialog(FloatLayout):
 	convert = ObjectProperty(None)
 	cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    #savefile = ObjectProperty(None)
    convertfile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def function(self):
	    i = 0
	    WAV_FILE = path.join(path_dir)
	    extension = ""
	    extension = WAV_FILE.split(".")[-1]
	    text_file =("sample.txt","w")
	    if (extension != "wav"):
	        os.system("avconv -i " + WAV_FILE + " -vn -f wav temp.wav")
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
	    print(end)
	    while(start != end):
	        i+=1
	        with sr.WavFile(WAV_FILE) as source:
	            audio = r.record(source,end_time, start)
	            start += 4.0
	            end_time += 4.0
	        try:
	            print(i,"\n",start," --> ",end_time , r.recognize_google(audio)),
	        except sr.UnknownValueError:
	            print "",
	        except sr.RequestError as e:
	            print("Could not request results from Google Speech Recognition service; {0}".format(e))
	    os.remove("temp.wav")
	    return 0

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

   # def show_save(self):
    #    content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
     #   self._popup = Popup(title="Save file", content=content,
      #                      size_hint=(0.9, 0.9))
       # self._popup.open()

    def show_convert(self):
     	content = ConvertDialog(convert=self.convert, canscel=self.dismiss_popup)
     	self._popup = Popup(title="Convert file", content=content , size_hint=(0.9, 0.9) )
     	self._popup.open();

    def load(self, path, filename):
        path_dir = os.path.join(path, filename[0])

        self.dismiss_popup()

    #def save(self, path, filename):
     #   with open(os.path.join(path, filename), 'w') as stream:
      #      stream.write(self.text_input.text)
		
	    #self.dismiss_popup()

	button1 = Button('convert')
	button1.bind(function())
    def convert(self,path,filename):
    	path_dir = os.path.join(path, filename[0])
    	self.function()
    	
    	self.dismiss_popup()


class Editor(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
#Factory.register('SaveDialog', cls=SaveDialog)
Factory.register('ConvertDialog', cls=ConvertDialog)

if __name__ == '__main__':
    Editor().run()