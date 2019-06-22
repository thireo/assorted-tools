from kivy.app import App
from kivy.uix.button import Button
import subprocess
import os
import signal

class TestApp(App):
	global p
	def press(self,instance):
		print('yoyoyoy')
		self.p = subprocess.Popen(["../Scripts/test.sh"]).pid
		print(self.p)
	def release(self,instance):
		print('sdf')
		os.kill(self.p,signal.SIGKILL)
	def build(self):
		mButton = Button(text='Hello World')
		mButton.bind(on_press=self.press)
		mButton.bind(on_release=self.release)
		return mButton
TestApp().run()
