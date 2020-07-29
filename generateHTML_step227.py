from tkinter import *
import generateHTML_userMakeWebpage as mainProgram

def makeHTML(self):
    userText = retrieve_input(self)
    f = open("demofile2.html", "a")
    f.write("<html> \n<body> \n{} \n</body> \n</html>".format(userText))
    f.close()

    #open and read the file after the appending:
    f = open("demofile2.html", "r")
    print(f.read())

def retrieve_input(self):
    self.userData = self.txt_browse1.get()
    return self.userData
