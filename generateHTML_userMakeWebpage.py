
from tkinter import *
import tkinter as tk


import generateHTML_step227 as functionDoc


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(520,250) #(Width, Height)
        self.master.maxsize(520,250)
        self.master.title("Browse")
        self.master.configure(bg="#F0F0F0")

        
        self.btn_browse1 = tk.Button(self.master,width=17,height=2,text='Put text in document >',command=lambda: functionDoc.makeHTML(self))
        self.btn_browse1.grid(row=0,column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    

        self.txt_browse1 = tk.Entry(self.master,width=28,text='Decide what text you want in your page!: ')
        self.txt_browse1.grid(row=0,column=4,padx=(30,20),pady=(25,0),sticky=N+E+W)

        



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
