#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as mbox
from tkinter import messagebox
import sys 
# this is a comment
class GuiBaseClass():
  
  def __init__(self,root):
      
      # create widgets
      self.root=root
      self.menu=dict()
      self.menubar = tk.Menu(self.root,tearoff=0)
      menu_file = tk.Menu(self.menubar,tearoff=0)
      menu_help  = tk.Menu(self.menubar,tearoff=0)
      
      # fix menubar -> self.menubar
      self.menubar.add_cascade(menu=menu_file,label='File',underline=0)
      menu_file.add_separator()
      #adding a sub menu
      menu_file.add_command(label='Open', command=self.openFile, underline=1)
      menu_file.add_command(label='Exit',  command=self.exit,underline=1)
      
      # Help menu
      self.menubar.add_cascade(menu=menu_help,label='Help',underline=0)
      menu_help.add_separator()
      menu_file.add_command(label='Open', command=self.openFile, underline=1)
      menu_help.add_command(label='About', command=self.about,underline=1)
      self.menu['menubar'] = self.menubar
      self.menu['File']    = menu_file
      self.menu['Help']    = menu_help
      
      # fix connect root with menubar
      self.root.config(menu=self.menubar)
      #self.menubar.option_add('*tearOff', 0)    
      
      # create ttk.Frame (self.frame)
      self.frame=ttk.Frame(self.root)
      self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
  # def pand(self):
  #     self.panedwindow = ttk.PanedWindow(self.root,orient='horizontal')
  #     self.panedwindow.pack(side='top', fill='both', expand=True)   


  def openFile(self):
    filepath = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("dat files", "*.dat"),("all files", "*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()    

  def mainLoop(self):
      self.root.mainloop()

  def about (self): 
      mbox.showinfo(title="GuiBaseClass",message='About GuiBaseClass\nVersion: 1.0\nOdCh\n2022') 

  def getRoot(self):
      return self.root      
  
  def getFrame(self):
      return(self.frame)

  def getPanedWindow(self):
      return self.panedwindow      
  
  def getMenu(self,entry):
      if entry in self.menu:
        return (self.menu[entry])
      else:
        last = self.menu['menubar'].index('end')
        self.menu[entry]= tk.Menu(self.menubar)
        self.menu['menubar'].insert_cascade(
          last, menu=self.menu[entry],label=entry)
        return(self.menu[entry])
  
  def exit(self,ask=True):
        mbox = messagebox.askyesno('exit', 'Are you sure you want to exit?')
        if mbox:
            self.root.destroy()
            sys.exit(0)

if __name__ == '__main__':
    root=tk.Tk()
    bapp = GuiBaseClass(root)
    mnu=bapp.getMenu('Edit')
    mnu.add_command(label='Copy',command=lambda: print('Copy'))
    
    # example for using getFrame
    frm=bapp.getFrame()
    btn=ttk.Button(frm,text="Button X",command=lambda: sys.exit(0))
    btn.pack()
    bapp.mainLoop()
    # example for using getMenu

