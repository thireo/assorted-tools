from kivy.app import App
from kivy.uix.button import Button
import subprocess
import os
import signal
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from subprocess import PIPE, Popen

#Config.set('graphics','width','20')
#Config.set('graphics','height','20')
#Config.write()

class TestApp(App):
	global p
	global b
	def press(self,instance):
		print('yoyoyoy')
		self.p = Popen(["../Scripts/test.sh"],stdout=PIPE)
		self.p = self.p.pid()
#		self.b = self.p.communicate()[0]
#		while(1):
#			print(self.b)
#		text = self.p.communicate()[0]
#		self.b = check_output("../Scripts/test.sh")
		print(self.p)
	def release(self,instance):
		print('sdf')
		os.kill(self.p,signal.SIGKILL)
#		os.kill(self.b,signal.SIGKILL)
	def stopiness(self,instance):
		App.get_running_app().stop()
	def build(self):
		layout = GridLayout(cols=3, row_force_default=True, row_default_height=100)
		mButton = Button(text='Start ECM DK')
		mButton.bind(on_press=self.press)
		mButton.bind(on_release=self.release)
		#mButton.size = (10,10)
		layout.add_widget(mButton)
		layout.add_widget(Button(text='CLEAN'))
		btn = Button(text='EXIT')
		btn.bind(on_press=self.stopiness)
		layout.add_widget(btn)
		return layout
#Window.size = (150,100)
TestApp().run()

