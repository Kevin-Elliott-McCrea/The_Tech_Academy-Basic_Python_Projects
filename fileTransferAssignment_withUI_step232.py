

from tkinter import *
import tkinter as tk


import fileTransferAssignment2_step232 as movFunction



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        self.master = master
        self.master.minsize(520,250)
        self.master.maxsize(520,250)
        self.master.title("File Transfer Assignment")
        self.master.configure(bg="#F0F0F0")

        
        self.btn_browse1 = tk.Button(self.master,width=17,height=2,text='Select Src Folder >',command=lambda: movFunction.browse_button(self))
        self.btn_browse1.grid(row=0,column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    
        self.btn_browse2 = tk.Button(self.master,width=17,height=2,text='Select Dst Folder >',command=lambda: movFunction.browse_button2(self))
        self.btn_browse2.grid(row=1,column=0,padx=(20,0),pady=(10,0),sticky=N+W)

        self.entry1 = tk.Entry(self.master,width=28,text="")
        self.entry1.grid(row=0, column=1)

        self.entry2 = tk.Entry(self.master,width=28,text="")
        self.entry2.grid(row=1,column=1,padx=(30,20),pady=(25,0),sticky=N+E+W)


        self.btn_browse3 = tk.Button(self.master,width=17,height=2,text='Initiate file transfer',command=lambda: movFunction.initiateFileTransfer(self))
        self.btn_browse3.grid(row=4,column=0,padx=(20,0),pady=(10,0),sticky=N+W)


#brwsFunction = movFunction.browse_button(self)
#print(brwsFunction.srcFolder_Path)

        



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

