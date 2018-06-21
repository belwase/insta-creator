#!/usr/bin/env python

"""splash.py: Class for creating splash screen."""
__author__ = "Ashish Belwase"


from tkinter import *
from tkinter import font
import time


class SplashScreen():

	def __init__(self, settings):
		self.master = Tk()
		self.master.title("Loading %s"%(settings['APP_NAME']))
		self.master.geometry("400x400+300+100")
		self.master.resizable(0,0)
		self.master.config(bg = "#4267B2")
		self.master.overrideredirect(1)
		self.someFont = font.Font(family='Verdana', size=25, weight='bold')
		self.empty_canvas = Canvas(self.master,width = 400,height=250,bg = "#4267B2",highlightthickness=0).grid(row = 1,column = 1)
		self.lab1 = Label(self.empty_canvas,bg = "#4267B2",text = settings['APP_NAME'],font = self.someFont,fg = "#fff").grid(row = 1,column=1)
		self.loader_canvas = Canvas(self.master,width = 400,height=20,bg = "#4267B2",highlightthickness=0)
		self.loader_canvas.grid(row = 2,column = 1)
		self.lab2 = Label(self.empty_canvas,bg = "#4267B2",text = 'Developed by %s'%settings['APP_DEVELOPER'],font = ("Verdana", 10),fg = "#fff").grid(row = 3,column=1)

		loader_value = 50

		while loader_value < 400:
			self.loader = self.loader_canvas.create_rectangle(10,5,loader_value,2,fill = "#fff",width=0)
			loader_value += 50
			time.sleep(0.1)
			self.master.update()

		time.sleep(1)
		self.master.destroy()