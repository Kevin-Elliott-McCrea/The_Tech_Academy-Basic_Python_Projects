import os, time, shutil, sys

for f in os.listdir('C:\\Users\\kleib_000\\Desktop\\GitHub\\Python_Projects\\The_Tech_Academy-Basic_Python_Projects\\The_Tech_Academy-Basic_Python_Projects\\Destination_Folder'):
    print(f)
    ftime = os.path.getmtime(f)
    print(ftime)
    ctime_dir = str(ftime.tm_year), '-', str(ftime.tm_mon), '-', str(ftime.tm_mday)
    if not os.path.isdir(ctime_dir):
        os.mkdir(ctime_dir)
    dst = ctime_dir('C:\\Users\\kleib_000\\Desktop\\GitHub\\Python_Projects\\The_Tech_Academy-Basic_Python_Projects\\The_Tech_Academy-Basic_Python_Projects\\Copies' + f)
    shutil.move(f, dst);
    print('File' + f + 'has been moved to' + dst)

    
