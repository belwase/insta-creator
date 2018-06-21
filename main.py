#!/usr/bin/env python

"""main.py: Main entry point for Insta Creator Bot."""

__author__ = "Ashish Belwase"
__version__ = "1.0.1"
__email__ = "techackernp@gmail.com"
__status__ = "Production"


from tkinter import *
from tkinter import messagebox
from views.formmain import FormMain
from views.splash import SplashScreen
from modules.helper import *
import logging
from datetime import datetime
import json
import os


class App:

	def __init__(self, settings):


		self.master = Tk()
		#self.master.iconbitmap('images/favicon.ico')
		self.master.settings = settings
		self.currentWindow = FormMain(self.master)

	def run(self):
		self.master.mainloop()


if __name__ == '__main__':
	try:
		try:
			settings = load_settings()
			settings['APP_NAME'] = 'Insta Creator'
			settings['APP_DEVELOPER'] = 'belwasetech.com'


		except Exception as ex:
			root = Tk().withdraw()  # hiding the main window
			messagebox.showerror("Error", "Invalid settings.json File.")
			print ('Invalid JSON' , ex)
			#root.destroy()
		else:
			SplashScreen(settings)
			app = App(settings)
			app.run()
	except Exception as ex:
		messagebox.showerror("Error", ex)