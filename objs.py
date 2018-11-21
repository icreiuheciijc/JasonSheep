#objs

import tkinter as tk

# It is said that creating different
# files for every class is good, duh

# That was grammatically incorrect but lines up well

class cell:

    # Oh look a class that doesn't inherit anything from tkinter, how special!
    def __init__(self,root,key,value,path,compiler):
        self.compiler=compiler
        self.path=path
        self.frame=tk.Frame(root,bg='#3F444E',height=50,width=100)
        self.frame.bind('<Button-1>',self.focus)
        self.frame.pack_propagate(False)
        self.key_box=tk.Entry(self.frame,bg='#1F242E',bd=0,fg='#EEE',relief='flat')
        self.key_box['highlightthickness']=1
        self.key_box['insertbackground']='#FFF'
        self.key_box.insert(0,key)
        self.key_box.pack(side='left',padx=10)
        tk.Label(self.frame,text=':',bg='#3F444E',fg='#FFF').pack(side='left')
        self.value_box=tk.Entry(self.frame,bg='#1F242E',bd=0,fg='#EEE',relief='flat')
        self.value_box['highlightthickness']=1
        self.value_box['insertbackground']='#FFF'
        self.value_box.insert(0,value)
        self.value_box.pack(side='left',padx=10)

    def pack(self):
        self.frame.pack(fill='x',anchor='n',side='top')

    def focus(self,event):
        self.frame.focus()
        self.compiler()
