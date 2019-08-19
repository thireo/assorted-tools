from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.utils import get_color_from_hex
import subprocess
import os
import signal
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from subprocess import PIPE, Popen
from threading import Thread
from time import sleep


#Config.set('graphics','width','20')
#Config.set('graphics','height','20')
#Config.write()

txt1 = Label(text="hello bob")
txt2 = Label(text="")

char_limit = 25










class TestApp(App):
	global p
	global b
	global thread
	global mButton
	global chosenAPK




	def langSelecter(self):
		if(self.languages.text == "DK"):
			print("ecm21.apk")
			self.chosenAPK = "ecm21.apk"
			self.mButton.text = "Installér Dansk ECM"
		elif(self.languages.text == "DE"):
			print("ecmde21.apk")
			self.chosenAPK = "ecmde21.apk"
			self.mButton.text = "Installér Tysk ECM"
		elif(self.languages.text == "UK"):
			print("ecmuk21.apk")
			self.chosenAPK = "ecmuk21.apk"
			self.mButton.text = "Installér UK ECM"
		elif(self.languages.text == "SE"):
			print("abse21.apk")
			self.chosenAPK = "abse21.apk"
			self.mButton.text = "Installér Svensk ECM"
		elif(self.languages.text == "NO"):
			print("abno21.apk")
			self.chosenAPK = "abno21.apk"
			self.mButton.text = "Installér Norsk ECM"
		elif(self.languages.text == "NL"):
			print("qv21.apk")
			self.chosenAPK = "qv21.apk"
			self.mButton.text = "Installér Hollandsk ECM"
		else:
			print("bob")
	
	
	languages = Spinner(
		text='Vælg sprog her:',
		values=('DK','DE','SE','NO','NL','UK'),
		text_autoupdate=True)
	
	def show_selected_value(self, text):
		print('The spinner', self.languages, 'has text', text)
	

	def test(self):
		self.langSelecter()
		bob = subprocess.run(['adb','devices','-l'],capture_output=True)
		stdout = bob.stdout.decode('utf-8').split('\n')
		print(stdout)
		if(stdout.__len__() > 1):
			print(stdout[1])
			print("Found: ")
			txt1.text = "Fandt: " + stdout[1].split(':')[1]
		else:
			txt1.text = "Ingen telefon fundet"+self.languages.text
			print("No phone found...")
			#subprocess.run(['adb','wait-for-device'])
			return
		#print(bob.stdout.decode('utf-8'))
		print("return code:\t",bob.returncode)
		if(bob.returncode != 0):
			return

		bob = subprocess.run(['adb','shell','cmd','package','uninstall','dk.danishcare.epicare.mobile2'],capture_output=True)
		print(bob.stdout.decode('utf-8'))
		print("Uninstallation:\t",bob.returncode)
		txt1.text = "Afinstallerer ECM"
		"""if(bob.returncode != 0):
			#txt2.text = "ERROR: Couldn't uninstall ECM"
			print("ERROR: Couldn't uninstall ECM")
			return bob.returncode"""
		#sleep(5)


		bob = subprocess.run(['adb','install','-r','-g','-d',self.chosenAPK],capture_output=True)
		print(bob.stdout.decode('utf-8'))
		subprocess.run(['ls','-l'])
		print("Installation:\t",bob.returncode)
		txt1.text = "Installere ECM"#bob.stdout.decode('utf-8')
		if(bob.returncode != 0):
			txt2.text = "FEJL: Kunne ikke installere ECM"+"\n"+bob.stderr.decode('utf-8')
			txt1.text = "KONTAKT Andreas"
			print("ERROR: Couldn't install ECM")
			return bob.returncode

		txt1.text = "Giver fornødne rettigheder"
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
		print("Permissions granted:\t",bob.returncode)
		txt1.text = bob.stdout.decode('utf-8')
		txt1.text = "Nægter batteri optimering for ECM"
		subprocess.run(['adb','shell','dumpsys','deviceidle','whitelist','+dk.danishcare.epicare.mobile2'],capture_output=True)
		txt1.text = "Sætter ECM som standard opkaldsapp"
		subprocess.run(['adb','shell','settings','put','secure','dialer_default_application','dk.danishcare.epicare.mobile2'],capture_output=True)
		txt1.text = "Åbner ECM app"
		subprocess.run(['adb','shell','am','start','-n','dk.danishcare.epicare.mobile2/.EpiCareFreeActivity'],capture_output=True) 

		#subprocess.run(['adb','shell','am','broadcast','-a','dk.danishcare.epicare.mobile2.tts','--ei','dk.danishcare.epicare.mobile2.tts.key','0x2a2a'],capture_output=True)
		#subprocess.run(['adb','shell','reboot','-p'],capture_output=True)

		txt1.text = "All done. Ready for the next :) "
		return


	def press(self,instance):
		print('Pressed')
		#self.p = Popen(["../Scripts/test.sh"],stdout=PIPE)
		#self.p = self.p.pid()
#		self.b = self.p.communicate()[0]
#		while(1):
#			print(self.b)
#		text = self.p.communicate()[0]
#		self.b = check_output("../Scripts/test.sh")
# 		#print(self.p)
		#test(self)
	def release(self,instance):
		print('Released')
		self.thread = Thread(target=self.test)
		self.thread.start()
		#App.get_running_app().consommables.append("done")
		#exit()
		#os.kill(self.p,signal.SIGKILL)
#		os.kill(self.b,signal.SIGKILL)
	def stopiness(self,instance):
		#self.thread.stop()
		try:
			if(self.thread.is_alive()):
				txt1.text = "Closing..."
				self.thread.join(2)
		except AttributeError:
			print("AttributeError. thread not initialised.")
		App.get_running_app().stop()
	def build(self):
		layout = GridLayout(cols=3, row_force_default=True, row_default_height=100)
		self.mButton = Button(text='Start ECM DK')
		self.mButton.bind(on_press=self.press)
		self.mButton.bind(on_release=self.release)
		#mButton.size = (10,10)
		layout.add_widget(self.languages)
		#self.mButton.text = languages.text
		layout.add_widget(self.mButton)
		layout.add_widget(Button(text='CLEAN'))
		btn = Button(text='EXIT')
		btn.bind(on_press=self.stopiness)
		layout.add_widget(btn)
		#self.languages.on_text = self.langSelecter()
		layout.add_widget(txt1)
		layout.add_widget(txt2)
		txt2.color = get_color_from_hex("#FF0000")

		chosenAPK = ""
		return layout
#Window.size = (150,100)
TestApp().run()
#self.languages.bind(text=show_selected_value)




