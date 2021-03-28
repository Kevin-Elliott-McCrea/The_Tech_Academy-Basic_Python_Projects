import shutil
import os

source = 'C:\\Users\\kleib_000\\Desktop\\folderA\\'

destination = 'C:\\Users\\kleib_000\\Desktop\\folderB\\'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
