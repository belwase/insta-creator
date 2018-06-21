#!/usr/bin/env python

"""ui_builder.py: Class for creating custom UI Widget."""
__author__ = "Ashish Belwase"

from tkinter import *
from tkinter import ttk


class Builder:

    def __init__(self, master):
        self.master = master
        self.style = ttk.Style()
        self.defaults = {
            'label':{'fg':'#365899', 'bg':'#E9EBEE'},
            'button':{'fg':'#F2FFFF', 'bg':'#3B5970', 'activebackground':'#365899', 'activeforeground':'#F2FFFF', 'cursor':'hand2'}
        }

        self.style.configure("E1.TEntry", padding=(5,0,0,0))

    def createLabel(self, data):
        style = data['label']['style']
        grid = data['label']['grid']
        label = Label(style.get('frame',self.master),  font=style.get('font','TkDefaultFont'), text=style['text'], anchor=style.get('anochor','w'), justify=style.get('justify',LEFT), fg=style.get('fg', self.defaults['label']['fg']) ,bg=style.get('bg', self.defaults['label']['bg']))
        label.grid(row=grid['row'], column=grid.get('column',0),padx=grid.get('padx',0),pady = grid.get('pady', 5), sticky=grid.get('sticky',W)) #,sticky=grid.get('sticky',E) ,pady = grid.get('pady', 5),padx=grid.get('padx',90))
        return label
    
    def createTextBox(self, data, label=True, read_only=False):
        if label:
            l = self.createLabel(data)

        style = data['entry']['style']
        grid = data['entry']['grid']
        entry = ttk.Entry(style.get('frame',self.master), show=style.get('show', ''), style=style.get('estyle',''), justify=style.get('justify',LEFT), textvariable=style['textvariable'], width=style.get('width',25))
        if read_only:
            entry.config(state=DISABLED)
        entry.grid(row=grid['row'], column=grid.get('column',0),sticky=grid.get('sticky',W), padx=grid.get('padx',0), pady=grid.get('pady',5), ipadx=grid.get('ipadx', 0) ,ipady=grid.get('ipady',5))

        if 'button' in data.keys():
            self.createButton(data)

        return entry

    def createButton(self, data, label=False):
        if label:
            self.createLabel(data)
        style = data['button']['style']
        grid = data['button']['grid']
        button = Button(
            style.get('frame',self.master),
            text=style['text'], command=style['callback'],
            height=style.get('height',1),
            width=style.get('width',7),
            font=style.get('font', 'TkDefaultFont'),
            bg=style.get('bg',self.defaults['button']['bg']),fg=style.get('fg',self.defaults['button']['fg']),
                  cursor=style.get('cursor',self.defaults['button']['cursor']),activebackground=style.get('activebackground',self.defaults['button']['activebackground']),activeforeground=style.get('activeforeground',self.defaults['button']['activeforeground']) )
        button.grid(row=grid['row'], column=grid.get('column',0),sticky=grid.get('sticky',S), padx=grid.get('padx',0), pady=grid.get('pady',0))


    def createCheckBox(self, data):
        style = data['style']
        grid = data['grid']
        
        checkbox = Checkbutton(
            style.get('frame', self.master),
            text=style.get('text', ''), variable=style.get('variable'),onvalue=1, offvalue="L"
        )
        checkbox.grid(row=grid['row'], column=grid.get('column',0),sticky=grid.get('sticky',S), padx=grid.get('padx',0), pady=grid.get('pady',0))