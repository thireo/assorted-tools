from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
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






def test(self):
	bob = subprocess.run(['adb','devices','-l'],capture_output=True)
	stdout = bob.stdout.decode('utf-8').split('\r\n')
	print(stdout[1])
	#print(bob.stdout.decode('utf-8'))
	print("return code:\t",bob.returncode)

	bob = subprocess.run(['adb','shell','cmd','package','uninstall','dk.danishcare.epicare.mobile2'],capture_output=True)
	print(bob.stdout.decode('utf-8'))
	print("return code:\t",bob.returncode)

	bob = subprocess.run(['adb','install','-r','-g','-d','ecm21.apk'],capture_output=True)
	print(bob.stdout.decode('utf-8'))
	print("return code:\t",bob.returncode)

	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.WRITE_EXTERNAL_STORAGE'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.READ_CALL_LOG'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.BLUETOOTH'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.BLUETOOTH_ADMIN'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.WAKE_LOCK'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.RECEIVE_BOOT_COMPLETED'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.CALL_PHONE'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.READ_PHONE_STATE'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.MODIFY_AUDIO_SETTINGS2'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.SEND_SMS'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.READ_CONTACTS'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.VIBRATE'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.ACCESS_COARSE_LOCATION'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.ACCESS_FINE_LOCATION'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.ACCESS_NETWORK_STATE'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.INTERNET'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.PROCESS_OUTGOING_CALLS'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS'],capture_output=True)
	subprocess.run(['adb','shell','pm','grant','dk.danishcare.epicare.mobile2','android.permission.READ_EXTERNAL_STORAGE'],capture_output=True)

	print(bob.stdout.decode('utf-8'))
	print("return code:\t",bob.returncode)

	subprocess.run(['adb','shell','dumpsys','deviceidle','whitelist','+dk.danishcare.epicare.mobile2'],capture_output=True)

	subprocess.run(['adb','shell','settings','put','secure','dialer_default_application','dk.danishcare.epicare.mobile2'],capture_output=True)
	subprocess.run(['adb','shell','am','start','-n','dk.danishcare.epicare.mobile2/.EpiCareFreeActivity'],capture_output=True) 

	#subprocess.run(['adb','shell','am','broadcast','-a','dk.danishcare.epicare.mobile2.tts','--ei','dk.danishcare.epicare.mobile2.tts.key','0x2a2a'],capture_output=True)
	#subprocess.run(['adb','shell','reboot','-p'],capture_output=True)





class TestApp(App):
	global p
	global b
	def press(self,instance):
		print('yoyoyoy')
		#self.p = Popen(["../Scripts/test.sh"],stdout=PIPE)
		#self.p = self.p.pid()
#		self.b = self.p.communicate()[0]
#		while(1):
#			print(self.b)
#		text = self.p.communicate()[0]
#		self.b = check_output("../Scripts/test.sh")
# 		#print(self.p)
		test(self)
	def release(self,instance):
		print('sdf')
		#exit()
		#os.kill(self.p,signal.SIGKILL)
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
		txt1 = Label(text="hello bob")
		layout.add_widget(txt1)
		return layout
#Window.size = (150,100)
TestApp().run()




