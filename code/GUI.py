#!/usr/bin/env python3

# Name: Odajiri Chinyere
# Matrikel Number: 811464

import re 
import os;
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as mbox
from tkinter import messagebox
import sys
from guibaseclass import GuiBaseClass
# this is a comment


class UniprotGui(GuiBaseClass):

    def __init__(self):
        """Initialize attributes of the parent Class."""
        super().__init__(root)
        self.texts = tk.StringVar()
        self.pubData = {};

    def openFile(self):
        self.pubData = {};
        filepath = filedialog.askopenfilename(
            initialdir="/", title="Select A File", filetypes=(("dat files", "*.dat"), ("all files", "*.*")))
        file = open(filepath, 'r')
        curFilename = os.path.basename(file.name) 
        self.texts.set(curFilename)

        goContents = [];
        flag = False;
        res="";
        curId = "";
        for line in file:
            curPubId = "";
            if re.match("^ID",line) or re.match("^RX",line) or re.match("^//",line):
                if(re.match("^ID",line)):
                    curId = line.split(" ")[3];
                elif(re.match("^RX",line)):
                    curPubId = line.split(" ")[3].split("=")[1].split(";")[0];
                    if curPubId in self.pubData.keys(): # check if the currrent pub id exists in our key list
                        self.pubData[curPubId].append(curId); # add to the list of current Pub Id
                    else:
                        self.pubData[curPubId] = [curId]; # Create a new Key and add a list with the current Id.
                else:
                    curId = "";
                    curPubId = "";
        # print(self.pubData);
        file.close()

    def showRes(self):
        searchVal = self.e1.get();
        self.e1.delete(0,END)
        self.l1.delete(0,END)
        if(searchVal in self.pubData.keys()):
            for item in self.pubData[searchVal]:
                self.l1.insert(END, item)
        else:
            mbox.showinfo(title="Search Error",message="Sorry No such data / record exists in the system... \nPlease try a different one.");

    def layout(self):
        ##########################
        row1 = tk.Frame(self.root)
        lFrame = ttk.LabelFrame(row1, text="Ref Search")
        lFrame.pack(fill="both", side="left", expand=True)

        self.e1 = tk.Entry(lFrame)
        self.e1.pack(fill="both", side="left", expand=True)

        self.b1 = tk.Button(lFrame, text="Search",command=self.showRes)
        self.b1.pack(fill="both", side="left", expand=True)
        # self.b1.command();
        row1.pack(fill="both", expand=True)
        pass
        ###############################
        row2 = tk.Frame(self.root)
        self.l1 = tk.Listbox(row2)
        self.l1.pack(fill="both", side="left", expand=True)

        self.scroll_bar = ttk.Scrollbar(row2)
        self.scroll_bar.pack( side = LEFT,fill = BOTH )
        # mylist = Listbox(root, yscrollcommand = scroll_bar.set )
        self.l1.config( yscrollcommand = self.scroll_bar.set)
        self.scroll_bar.config(command =  self.l1.yview)


        self.text = tk.Text(row2) 
        self.text.pack(fill="both", side="left", expand=True)
        row2.pack(fill="both", expand=True)

        ##############################
        row3 = tk.Frame(self.root)
        self.lab = ttk.Label(row3, textvariable=self.texts)
        # self.lab['text'] = "Text updated"
        self.lab.pack(fill="both", side="left", expand=True)

        self.prog = ttk.Progressbar(row3, orient='horizontal', mode='indeterminate', length=280)
        self.prog.pack(fill="both", side="left", expand=True)
        row3.pack(fill="both", expand=True)


if __name__ == '__main__':
    root = tk.Tk()
    bapp = UniprotGui()
    mnu = bapp.getMenu('Edit')
    mnu.add_command(label='Copy', command=lambda: print('Copy'))
    # bapp.getE()
    # bapp.but()
    bapp.layout()

    # # example for using getFrame
    # frm=bapp.getFrame()
    # btn=ttk.Button(frm,text="Button X",command=lambda: sys.exit(0))
    # btn.pack()
    bapp.mainLoop()
