#objs

import tkinter as tk

# It is said that creating different
# files for every class is good, duh

# That was grammatically incorrect but lines up well

class Cell:

    # Oh look a class that doesn't inherit anything from tkinter, how special!
    def __init__(self,root,key,value,path,compiler,alert):
        self.alert=alert
        self.compiler=compiler
        self.path=path
        self.old_key_type='String'
        self.old_type='String'
        self.frame=tk.Frame(root,bg='#3F444E',height=50,width=100)
        self.frame.bind('<Button-1>',self.focus)
        self.frame.pack_propagate(False)

        # Fitting all config in the constructor makes the code
        # too long for my liking, thus the index configuration
        self.children=[]
        self.children_type=None
        self.key_type=tk.StringVar(root)
        self.key_type.set('String')
        self.key_value_type_box=tk.OptionMenu(self.frame,self.key_type,*['String'],command=self.focus)
        self.key_value_type_box['bg']='#3F444E'
        self.key_value_type_box['fg']='#000'
        self.key_value_type_box.pack(side='left',padx=10)
        self.key_value_type_box.config(width=10)
        self.key_box=tk.Entry(self.frame,bg='#1F242E',bd=0,fg='#EEE',relief='flat')
        self.key_box['highlightthickness']=1
        self.key_box['insertbackground']='#FFF'
        self.key_box.insert(0,key)
        self.key_box.bind('<FocusOut>',self.focus)
        self.key_box.pack(side='left',padx=10)
        tk.Label(self.frame,text=':',bg='#3F444E',fg='#FFF').pack(side='left')
        self.value_type=tk.StringVar(root)
        self.value_type.set('String')
        self.value_type_box=tk.OptionMenu(self.frame,self.value_type,*['String'],command=self.focus)
        self.value_type_box['bg']='#3F444E'
        self.value_type_box['fg']='#000'
        self.value_type_box.pack(side='left',padx=10)
        self.value_type_box.config(width=10)
        self.value_box=tk.Entry(self.frame,bg='#1F242E',bd=0,fg='#EEE',relief='flat')
        self.value_box['width']=20
        self.value_box['highlightthickness']=1
        self.value_box['insertbackground']='#FFF'
        self.value_box.insert(0,value)
        self.value_box.bind('<FocusOut>',self.focus)
        self.value_box.pack(side='left',padx=10)
        self.focus()

    def update_menu(self,key_opts,opts):
        self.key_value_type_box['menu'].delete(0,'end')
        self.value_type_box['menu'].delete(0,'end')
        for i in key_opts:
            self.key_value_type_box['menu'].add_command(label=i,command=lambda x=i:self.click_menu(self.key_type,x))
            
        for i in opts:
            self.value_type_box['menu'].add_command(label=i,command=lambda x=i:self.click_menu(self.value_type,x))

    def click_menu(self,menu,value): # See this is why I don't like tkinter
        menu.set(value)
        self.focus()

    def pack(self):
        self.frame.pack(fill='x',anchor='n',side='top')

    def validate(self):
        key=self.key_box.get()
        key_type=self.key_type.get()
        value=self.value_box.get()
        _type=self.value_type.get()
        if _type!=self.old_type: # Type change
            self.old_type=_type
            if _type in ['Array','Json']:
                self.children_type=_type
                self.value_box.pack_forget()
            else:
                self.children_type=None
                self.value_box.pack(side='left',padx=10)

        if key_type!=self.old_key_type: # Type change
            self.old_key_type=key_type
            return # For now
        
        # Alright here goes
        # Smart type conversion
        # Spaghetti alert
        
        conv={'String':lambda x:True,
              'Integer':lambda x:x.isdigit(),
              'Float':lambda x:x.replace('.','',1).isdigit(),
              'Boolean':lambda x:x in ['true','false'],
              'Array':lambda x:True,
              'Json':lambda x:True}

        new_key_types=[i for i in list(conv.keys())[:-2] if conv[i](key)]
        new_types=[i for i in conv if conv[i](value)]

        if not conv[key_type](key): self.key_type.set(new_key_types[-1])
        if not conv[_type](value): self.value_type.set(new_types[-1])
        self.update_menu(new_key_types,new_types)

    def get_value(self):
        conv={'String':lambda x:str(x),
              'Integer':lambda x:int(x),
              'Float':lambda x:float(x),
              'Boolean':lambda x:bool(x),
              'Array':lambda x:[],
              'Json':lambda x:{}}

        _type=self.type_box.get()
        value=self.value_box.get()
        return [_type,conv[_type](value)]
        
    def focus(self,event=None):
        self.frame.focus()
        self.validate()
        self.compiler()
