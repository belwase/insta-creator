from tkinter import *
import tkinter as tk
from tkinter import font  as tkfont
from functools import partial

class Form(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master

	def _initialize(self, master):
		pass

	def _initialize_view(self, master):
		pass

	def close(self):
		self.master.destroy()


class NavBar(tk.Frame):

    def __init__(self, parent, controller, builder):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.builder = builder
        
        self.builder.createLabel(
                {
                 'label':{'style':{'frame':self, 'text':'Insta Creator V1.0'},
                 'grid':{'row':5, 'column':1, 'padx':0, 'sticky':tk.W}
                 }
                }
            )


        self.builder.createButton(
        {
            'button':{
                'style':{'frame':self, 'text':'Single Creator', 'callback':lambda: controller.show_frame("StartPage"), 'height':1, 'width':10, 'font':'TkDefaultFont 16 bold', 'bg':'green', 'fg':'#F2FFFF', 'activebackground':'#365899', 'activeforeground':'#F2FFFF'},
                'grid':{'row':6, 'column':1, 'sticky':tk.W}
                }
        }
        )

        self.builder.createButton(
        {
            'button':{
                'style':{'frame':self, 'text':'Bulk Creator', 'callback':lambda: controller.show_frame("BulkCreator"), 'height':1, 'width':10, 'font':'TkDefaultFont 16 bold', 'bg':'green', 'fg':'#F2FFFF', 'activebackground':'#365899', 'activeforeground':'#F2FFFF'},
                'grid':{'row':7, 'column':1,  'sticky':tk.W}
                }
        }
        )

        self.builder.createButton(
        {
            'button':{
                'style':{'frame':self, 'text':'Settings', 'callback':lambda: controller.show_frame("SettingPage"), 'height':1, 'width':10, 'font':'TkDefaultFont 16 bold', 'bg':'green', 'fg':'#F2FFFF', 'activebackground':'#365899', 'activeforeground':'#F2FFFF'},
                'grid':{'row':8, 'column':1, 'sticky':tk.W}
                }
        }
        )

        self.builder.createButton(
        {
            'button':{
                'style':{'frame':self, 'text':'About', 'callback':lambda: controller.show_frame("AboutPage"), 'height':1, 'width':10, 'font':'TkDefaultFont 16 bold', 'bg':'green', 'fg':'#F2FFFF', 'activebackground':'#365899', 'activeforeground':'#F2FFFF'},
                'grid':{'row':9, 'column':1,  'sticky':tk.W}
                }
        }
        )
        

class StartPage(tk.Frame):

    def __init__(self, parent, controller, builder):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.builder = builder


        self.username = ''
        self.password = ''
        self.email = ''
        self.full_name = ''

        frame = tk.Frame(self, width=500, height=300)
        frame.pack(fill=tk.BOTH)


        # self.builder.createLabel(
        #         {
        #          'label':{'style':{'frame':frame, 'text':'This pro'}, 'grid':{'row':5, 'padx':10}
        #          }
        #         }
        #     )

        # self.builder.createLabel(
        #         {
        #          'label':{'style':{'frame':frame, 'text':'You must provide '}, 'grid':{'row':6, 'padx':0}}
        #          }
        #     )
        
        # label = tk.Label(frame, text="This is the start page", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)

        # button1 = tk.Button(frame, text="Go to Bulk Creator",
        #                     command=lambda: controller.show_frame("BulkCreator"))
        
        # button1.pack()

        self.builder.createTextBox(
            {
                'label':{'style':{'frame':frame,'text':'Username' , 'font':'TkDefaultFont 12 bold'}, 'grid':{'row':1, 'pady':5, 'sticky':tk.E}},
                'entry':{'style':{'frame':frame,'textvariable':self.controller.username, 'estyle':'E1.TEntry'}, 'grid':{'row':1,'column':2, 'pady':5, 'ipady':5, 'padx':5}},
            }
            )

        self.builder.createTextBox(
            {
                'label':{'style':{'frame':frame,'text':'Password' , 'font':'TkDefaultFont 12 bold'}, 'grid':{'row':2, 'pady':5, 'sticky':tk.E}},
                'entry':{'style':{'frame':frame,'textvariable':self.controller.password, 'estyle':'E1.TEntry'}, 'grid':{'row':2,'column':2, 'pady':5, 'ipady':5, 'padx':5}},
            }
            )

        self.builder.createTextBox(
            {
                'label':{'style':{'frame':frame,'text':'Email' , 'font':'TkDefaultFont 12 bold'}, 'grid':{'row':3, 'pady':5, 'sticky':tk.E}},
                'entry':{'style':{'frame':frame,'textvariable':self.controller.email, 'estyle':'E1.TEntry'}, 'grid':{'row':3,'column':2, 'pady':5, 'ipady':5, 'padx':5}},
            }
            )

        self.builder.createTextBox(
            {
                'label':{'style':{'frame':frame,'text':'Full Name' , 'font':'TkDefaultFont 12 bold'}, 'grid':{'row':4, 'pady':5, 'sticky':tk.E}},
                'entry':{'style':{'frame':frame,'textvariable':self.controller.fullname, 'estyle':'E1.TEntry'}, 'grid':{'row':4,'column':2, 'pady':5, 'ipady':5, 'padx':5}},
            }
            )

        self.builder.createButton(
        {
            'button':{
                'style':{'frame':frame, 'text':'Create', 'callback':self.controller.create_account, 'height':1, 'width':10, 'font':'TkDefaultFont 16 bold', 'bg':'green', 'fg':'#F2FFFF', 'activebackground':'#365899', 'activeforeground':'#F2FFFF'},
                'grid':{'row':5, 'column':2,  'sticky':tk.W}
                }
        }
        )



        self.controller.lbl_status_single = self.builder.createLabel(
                {
                 'label':{'style':{'frame':frame, 'text':'', 'fg':'red'},
                 'grid':{'row':6, 'column':2, 'padx':10, 'sticky':tk.W}
                 }
                }
            )


        self.controller.lbl_output_single = self.builder.createLabel(
                {
                 'label':{'style':{'frame':frame, 'text':'', 'fg':'red'},
                 'grid':{'row':8, 'column':2, 'padx':10, 'sticky':tk.W}
                 }
                }
            )
    



class BulkCreator(tk.Frame):

    def __init__(self, parent, controller, builder):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.builder = builder

        frame = tk.Frame(self, width=500, height=300)
        frame.pack(fill=tk.BOTH)


        self.controller.bulk_csv_input = self.builder.createTextBox(
            {
                'label':{'style':{'frame':frame, 'text':'Input CSV', 'font':'TkDefaultFont 12 bold'}, 'grid':{'row':2, 'sticky':tk.E}},
                'entry':{'style':{'frame':frame, 'textvariable':self.controller.sv_bulk_input_csv, 'width':55}, 'grid':{'row':2, 'column':1, 'padx':5}},
                'button':{ 'style':{'frame':frame, 'text':'Browse', 'callback':partial(self.controller._on_buttonupload_clicked, button='BULK_CSV_INPUT')}, 'grid':{'row':2, 'column':2, 'sticky':tk.W+tk.E, 'padx':5 } }
            },
            read_only=False
            )

        self.builder.createButton(
        {
            'button':{
                'style':{'frame':frame, 'text':'Create Bulk', 'callback':self.controller.create_account_bulk, 'height':1, 'width':10, 'font':'TkDefaultFont 16 bold', 'bg':'green', 'fg':'#F2FFFF', 'activebackground':'#365899', 'activeforeground':'#F2FFFF'},
                'grid':{'row':3, 'column':1,  'sticky':tk.W}
                }
        }
        )



        self.controller.lbl_status_bulk = self.builder.createLabel(
                {
                 'label':{'style':{'frame':frame, 'text':'', 'fg':'red'},
                 'grid':{'row':6, 'column':1, 'padx':10, 'sticky':tk.W}
                 }
                }
            )

        self.controller.lbl_output_bulk = self.builder.createLabel(
                {
                 'label':{'style':{'frame':frame, 'text':'', 'fg':'red'},
                 'grid':{'row':8, 'column':1, 'padx':10, 'sticky':tk.W}
                 }
                }
            )
    	
class SettingPage(tk.Frame):

    def __init__(self, parent, controller, builder):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.builder = builder

        frame = tk.Frame(self, width=500, height=300)
        frame.pack(fill=tk.BOTH)


        self.builder.createCheckBox(
            {
                'style':{'frame':frame,'text':'Use Proxy', 'variable':self.controller.use_proxy, 'font':'TkDefaultFont 12 bold'},
                'grid':{'row':2, 'column':1, 'sticky':tk.W},
            }
            )
