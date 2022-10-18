#!/usr/bin/env python3

# Name: Odajiri Chinyere
# Matrikel Number: 811464

from re import U, search
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as mbox
from tkinter import messagebox
import sys, os
from guibaseclass import GuiBaseClass
# this is a comment


class UniprotGui(GuiBaseClass):

    def __init__(self):
        """Initialize attributes of the parent Class."""
        super().__init__(root)
        self.text = tk.StringVar()
        #self.text.set("File Info")
        #File info would change when file is opened.


    def openFile(self,filepath=''):
        if (filepath == ''):
            filepath = filedialog.askopenfilename(
                initialdir="/", title="Select A File", filetypes=(("dat files", "*.dat"), ("all files", "*.*")))
        if filepath == '':
            return
        file = open(filepath, 'r')
        x = os.path.basename(file.name)
        print(x)
        self.text.set(x)
        file.close()

        
    def searchFile(self,filepath=''):
        file1 = filedialog.askopenfile()
        file2 = file1.name
        f = open(file2)
        #y =f.read()
        #print(y)
        #self.text.set(y)

    def get_value(self):
        file1 = filedialog.askopenfile()
        file2 = file1.name
        f = open(file2)        
        e_text=self.e1.get()
        Label(text=f, font= ('Century 15 bold')).pack(pady=20)    

        # x = os.path.basename(file.name)
        # print(x)
        # self.text.set(x)
        # file.close()        

    def layout(self):
        ##########################
        row1 = tk.Frame(self.root)
        lFrame = ttk.LabelFrame(row1, text="Ref Search")
        lFrame.pack(fill="both", side="left", expand=True)

        self.e1 = tk.Entry(lFrame)
        self.e1.pack(fill="both", side="left", expand=True)

        self.b1 = tk.Button(lFrame, text="Search",command = self.get_value)
        self.b1.pack(fill="both", side="left", expand=True)
        row1.pack(fill="both", expand=True)
        pass
        ###############################
        # row2 = tk.Frame(self.root)
        # self.l1 = tk.Listbox(row2)
        # self.l1.pack(fill="both", side="left", expand=True)
        # # self.text = tk.Text(row2)
        # # self.text.pack(fill="both", side="left", expand=True)
        # # self.scrol = ttk.Scrollbar(row2)
        # # self.scrol.pack()
        # row2.pack(fill="both", expand=True)

        ##############################
        row3 = tk.Frame(self.root)
        self.lab2 = ttk.Label(row3)
        self.lab2.pack(fill="both", side="left", expand=True)
        scroll_bar = Scrollbar(self.root)
        scroll_bar.pack( side = RIGHT,fill = Y )
        # mylist = Listbox(root, yscrollcommand = scroll_bar.set )
        # mylist = Listbox(root, yscrollcommand = scroll_bar.set )
        
        scroll_bar.config( command = self.lab2)

        
        row3.pack(fill="both", expand=True)

        #################################
        row4 = tk.Frame(self.root)
        self.lab = ttk.Label(row4, textvariable=self.text)
        
        #self.lab['text'] = "Text updated"
        self.lab.pack(fill="both", side="left", expand=True)
        

        self.prog = ttk.Progressbar(row4, orient='horizontal', mode='indeterminate', length=280)
        self.prog.pack(fill="both", side="left", expand=True)
        row4.pack(fill="both", expand=True)


if __name__ == '__main__':
    root = tk.Tk()
    bapp = UniprotGui()
    mnu = bapp.getMenu('Edit')
    mnu.add_command(label='Copy', command=lambda: print('Copy'))
    # bapp.getE()
    # bapp.but()
    bapp.layout()
    if (len(sys.argv)>1 and os.path.isfile(sys.argv[1])):
        bapp.openFile(sys.argv[1])
    # # example for using getFrame
    # frm=bapp.getFrame()
    # btn=ttk.Button(frm,text="Button X",command=lambda: sys.exit(0))
    # btn.pack()
    bapp.mainLoop()

