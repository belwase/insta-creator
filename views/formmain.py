#!/usr/bin/env python

"""formmain.py: Main Window Form."""
__author__ = "Ashish Belwase"


#from tkinter import *
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import filedialog, messagebox
from datetime import datetime
from functools import partial
import json
import os
import logging
import threading

from views.form import *
from views.ui_builder import Builder as UiBuilder
from modules.helper import *
from modules.insta import InstaBot


class UIHandler():

    @staticmethod
    def create_account(data, bulk=False):
        #print('up', use_proxy)
        ib = InstaBot()
        if bulk:
            response = ib.run_bulk(data)
        else:
            response = ib.run(data)
        return response


class FormMain(Form):

    def __init__(self, master):
        self.settings = master.settings
        self.default_files = True
        self.builder = UiBuilder(master)
        Form.__init__(self, master)
        self.reset_label()
        self._initialize(master)
        self._initialize_view(master)


    def _initialize(self, master):
        if not os.path.exists('logs'):
            os.makedirs('logs')
        if not os.path.exists('output'):
            os.makedirs('output')


        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.fullname = StringVar()
        self.sv_bulk_input_csv = StringVar()
        self.use_proxy = StringVar()

        self.bulk_input = []

        log_file  = 'logs/'+datetime.strftime(datetime.now(), '%Y-%m-%d_%H')+'.txt'
        fp = open(log_file, 'w')
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(levelname)s:%(asctime)s:%(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
            )
        self.logger = logging
        self.logger.info('%s Started..')


    def get_proxy_var(self):
        if self.use_proxy.get() == '1':
            return True
        return False

    def callback(self, sv):
        print (sv.get())

    def _on_buttonstart_clicked(self, event=None):
        pass

    def _on_buttonupload_clicked(self, event=None, button='BULK_CSV_INPUT'):
        filename = ''
        if button == 'OUTPUT_DIR':
            filename = filedialog.askdirectory()
        else:
            filename = filedialog.askopenfilename()
        print (filename)
        if filename != '':
            try:
                self.bulk_input = csvtoDict(filename)
                keys = self.bulk_input[0].keys()
                for k in ['fullname','username','password','email','proxy_ip_port','proxy_un_pw']:
                    if k not in keys:
                        messagebox.showwarning('Error', 'Missing field {} in csv file.'.format(k))
                        return
                self.sv_bulk_input_csv = StringVar(value=filename)
                self.bulk_csv_input.config(textvariable=self.sv_bulk_input_csv)

            except Exception as ex:
                print (ex)
                self.logger.error('Not a valid CSV File')
                messagebox.showwarning('Error', 'Not a valid csv file')

            
    def reset_label(self):
        ## reset all labels when create is clicked
        self.lbl_status_single = None
        self.lbl_status_bulk = None
        self.lbl_output_single = None
        self.lbl_output_bulk = None

    def _initialize_view(self, master):

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
        self.master.title(self.settings['APP_NAME'])
        self.master.geometry("800x450+50+100")
        self.master.config(bg='#E9EBEE')
        self.master.resizable(0,0)


       


        frame = NavBar(parent=master, controller=self, builder=self.builder)
        frame.grid(row=5, column=1, sticky="w")

        self.frames = {}
        for F in (StartPage, BulkCreator, SettingPage):
            page_name = F.__name__
            frame = F(parent=master, controller=self, builder=self.builder)
            self.frames[page_name] = frame
            frame.grid(row=5, column=5, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


    def _create_account(self):
        self.logger.info('Got signal to create single account')
        data = {
            'username': self.username.get(), 'password':self.password.get(), 'email':self.email.get(), 'fullname':self.fullname.get()
        }
        data = {
                'email' : 'test@gmail.com', #'test13411@gmail.com',
                'password' : '12eafe5678@12@',
                'fullname' : 'test g'
                }
        data['username'] = data['email'].split('@')[0]

        if data['username'] == '' or data['email'] == '' or data['password'] == '' or data['fullname'] == '':
            messagebox.showwarning("Warning", "Please enter all details")
        else:
            self.logger.info('Payload :: {}'.format(data))
            status = 'Creating account : {} ......'.format(data['email'])
            self.lbl_status_single.config(text=status)
            output_file = 'output/'+datetime.strftime(datetime.now(), '%Y-%m-%d_%H_%M')+'.csv'
            fp = open(output_file, 'w')
            self.lbl_output_single.config(text='Output File : {}'.format(output_file))
            #messagebox.showwarning("Info",status )

            response = UIHandler.create_account(data, bulk=False)
            self.logger.info('Response for {} :: {}'.format(data['email'], response))
            self.lbl_status_single.config(text=response['message'])
            listtoCSSV([response], output_file)


    def create_account(self,event=None):
        t = threading.Thread(target=self._create_account)
        t.start()

        

    def _create_account_bulk(self):
        self.logger.info('Got signal to create bulk account')
        self.logger.info('Payload :: {}'.format(len(self.bulk_input)))
        status = 'Creating bulk account.....'
        self.lbl_status_bulk.config(text=status)


        if len(self.bulk_input) < 1:
            messagebox.showwarning("Error", "No rows in CSV file")

        else:

            output_file = 'output/'+datetime.strftime(datetime.now(), '%Y-%m-%d_%H_%M')+'.csv'
            fp = open(output_file, 'w')
            self.lbl_output_bulk.config(text='Output File : {}'.format(output_file))
            response = UIHandler.create_account(self.bulk_input, bulk=True)
            listtoCSSV(response, output_file)

    def create_account_bulk(self,event=None):
        t = threading.Thread(target=self._create_account_bulk)
        t.start()
        
            