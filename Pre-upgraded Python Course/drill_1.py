
import os

path = "C:\\Users\\kleib_000\\Desktop\\GitHub\\Python_Projects\\The_Tech_Academy-Basic_Python_Projects\\PyProjects\\Python_drill_1"
dir_list = os.listdir(path)

print(dir_list)

for i in dir_list:
    if i.endswith('.txt'):
        array_paths = os.path.join(path, i)
        Jimbo = "Path: " + array_paths + " Date created/modified: " + str(os.path.getmtime(array_paths))
        print(Jimbo)
    






