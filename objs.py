#objs

import tkinter as tk

# It is said that creating different
# files for every class is good, duh

# That was grammatically incorrect but lines up well

class cell:

    # Oh look a class that doesn't inherit anything from tkinter, how special!
    def __init__(self,root,key,value,path,compiler,alert):
        self.alert=alert
        self.compiler=compiler
        self.path=path
        self.old_type='String'
        self.frame=tk.Frame(root,bg='#3F444E',height=50,width=100)
        self.frame.bind('<Button-1>',self.focus)
        self.frame.pack_propagate(False)
        self.key_box=tk.Entry(self.frame,bg='#1F242E',bd=0,fg='#EEE',relief='flat')
        # Fitting all configs in the constructor makes the code
        # ugly and fat like a poseidown, thus the index configs

        # Right that was a terrible joke no one will ever get that reference
        self.key_box['highlightthickness']=1
        self.key_box['insertbackground']='#FFF'
        self.key_box.insert(0,key)
        self.key_box.bind('<FocusOut>',self.focus)
        self.key_box.pack(side='left',padx=10)
        tk.Label(self.frame,text=':',bg='#3F444E',fg='#FFF').pack(side='left')
        self.value_box=tk.Entry(self.frame,bg='#1F242E',bd=0,fg='#EEE',relief='flat')
        self.value_box['highlightthickness']=1
        self.value_box['insertbackground']='#FFF'
        self.value_box.insert(0,value)
        self.value_box.bind('<FocusOut>',self.focus)
        self.value_box.pack(side='left',padx=10)
        self.type=tk.StringVar(root)
        self.type.set('String')
        self.type_box=tk.OptionMenu(self.frame,self.type,*['String'],command=self.focus)
        self.type_box['bg']='#3F444E'
        self.type_box['fg']='#000'
        self.type_box.pack(side='left',padx=10)
        self.type_box.config(width=10)
        self.focus()

    def update_menu(self,opts):
        self.type_box['menu'].delete(0,'end')
        for i in opts:
            self.type_box['menu'].add_command(label=i,command=lambda x=i:self.type.set(x))

    def pack(self):
        self.frame.pack(fill='x',anchor='n',side='top')

    def validate(self):
        value=self.value_box.get()
        _type=self.type.get()
        if _type!=self.old_type: # Type change
            self.old_type=_type
            return # For now
        
        # Alright here goes
        # Smart type conversion
        # Spaghetti alert
        
        conv={'String':lambda x:True,
              'Integer':lambda x:x.isdigit(),
              'Float':lambda x:x.replace('.','',1).isdigit(),
              'Boolean':lambda x:x in ['true','false']}
        
        new_types=[i for i in conv if conv[i](value)]

        if not conv[_type](value): self.type.set(new_types[-1])
        self.update_menu(new_types)      
        
    def focus(self,event=None):
        self.frame.focus()
        self.validate()
        self.compiler()
