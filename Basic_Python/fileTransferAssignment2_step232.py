from tkinter import filedialog
from tkinter import *
import tkinter as tk
import os, time, shutil, sys
from datetime import date
import fileTransferAssignment_withUI_step232


filename = ""
filename2 = ""
src = filename
dst = filename2


def browse_button(self):
    filename = filedialog.askdirectory()
    print(self.entry1.insert(INSERT,filename))
    global src
    src = filename
    
def browse_button2(self):
    filename2 = filedialog.askdirectory()
    print(self.entry2.insert(INSERT,filename2))
    global dst
    dst = filename2



def initiateFileTransfer(self):
    fileList = os.listdir(src)
    for f in fileList:
        print(f)
        ftime = os.path.getmtime(src + '/' + f)
        print(ftime)
        timeConversion = time.gmtime(ftime)
        print(timeConversion.tm_year)
        concatenatedTime = str(timeConversion.tm_year) + '-' + str(timeConversion.tm_mon) + '-' + str(timeConversion.tm_mday)
        print(concatenatedTime)
        today = date.today()
        currentTime = today.strftime("%Y-%#m-%#d")
        print("currentTime =", currentTime)
        print(type(concatenatedTime))
        print(type(currentTime))
        if concatenatedTime == currentTime:        
            shutil.move(src + '/' + f, dst);
            print('File' + f + 'has been moved to' + dst)
        else: print("No file has been moved\n")




# 1. Get a variable into the src and make it a string.
#   Also make sure the double slash works (try r for raw string or something else)

# 2. Do the same thing for dst

# 3. Put file check function into a button so user can activate at will
#
#
