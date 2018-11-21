# JasonSheep


# No Jason Yang this app isnt for
# you, I just thought it would be
# nice to do a pun with your name

# Normally I dont smack down long
# chunks of comments at the start
# of files, but since everyone on
# github and every where else are
# doing it and this make you look
# a pro so I'm also doing it even
# if it is, in this case, utterly
# pointless and grammatically bad

# Ooh wow this lines up very well


# 'You guys need to mark whenever
# you import dependencies because
# appearently whoever checks your
# code cannot see the huge import
# keyword before the line and you
# need to explicitly mark it, du'
# -(well my friend, you should be
# able to tell who said that ;) )

#Dependencies
import sys
import json
from objs import *
import tkinter as tk

#Oh look, a gui class named main_gui, what a surprise!
class main_gui:

    def __init__(self,root):

        #Initialize
        self.root=root
        self.size=(root.winfo_screenwidth(),root.winfo_screenheight()*0.875)
        self.cells=[]
        root.title('JasonSheep')
        root.geometry(('%dx%d')%self.size)
        root.resizable(width=True,height=True)
        root.bind('<Configure>',self.resize)

        #MainGUI
        self.bar=tk.Frame(root,bd=2,bg='#222',height=50)
        self.bar.bind('<Button-1>',self.remove_focus)
        self.bar.pack(fill='x')
        self.cell_holder=tk.Frame(root,bd=0,bg='#282C35',width=self.size[0]/2)
        self.cell_holder.bind('<Button-1>',self.remove_focus)
        self.cell_holder.pack(fill='y',expand=True,anchor='w',side='left')
        self.text_holder=tk.Frame(root,bd=0,bg='#21252C',width=self.size[0]/2)
        self.text_holder.bind('<Button-1>',self.remove_focus)
        self.text_holder.pack(fill='y',expand=True,anchor='e',side='right')

        #Menu
        self.menu=tk.Menu(root)
        
        file_menu=tk.Menu(self.menu)
        file_menu.add_command(label="Open")
        file_menu.add_separator()
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save As")
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=sys.exit)
        self.menu.add_cascade(label='File',menu=file_menu)

        root.config(menu=self.menu)
        self.add_cell(1,1)

    def resize(self,event):
        self.size=(root.winfo_width(),root.winfo_height()*0.875)
        self.cell_holder['width']=width=self.size[0]/2
        self.text_holder['width']=width=self.size[0]/2

    def add_cell(self,key,value,path=[]):
        self.cell_holder.pack_forget()
        cell(self.cell_holder,1,1,path,self.compile).pack()
        self.cell_holder.pack(fill='y',expand=True,anchor='w',side='left')

    def load(self,js): # YES JS STANDS FOR JSON HERE NOT JAVASCRIPT USE YA COMMON SENSE!
        d=json.load(js)

    def compile(self,update_text=True):
        pass

    def remove_focus(self,event):
        self.bar.focus()
        self.compile()

root=tk.Tk()
gui=main_gui(root)
root.mainloop()
