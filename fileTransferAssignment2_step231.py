import os, time, shutil, sys
from datetime import date
src = 'C:\\Users\\kleib_000\\Desktop\\GitHub\\Python_Projects\\The_Tech_Academy-Basic_Python_Projects\\The_Tech_Academy-Basic_Python_Projects\\Destination_Folder'
dst = 'C:\\Users\\kleib_000\\Desktop\\GitHub\\Python_Projects\\The_Tech_Academy-Basic_Python_Projects\\The_Tech_Academy-Basic_Python_Projects\\Copies'
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
