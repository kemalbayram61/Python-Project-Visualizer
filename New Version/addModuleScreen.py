import tkinter as tk
import tkinter.messagebox as msg
from tkinter import filedialog
from networkDefinition import ProjectNetwork
import parseOperations
import objectDefinition


class AddModuleScreen:
    __projectName = ""
    __networkName = ""
    __isAddModule = False

    def __init__(self,projectName,networkName):
        self.__projectName = projectName
        self.__networkName = networkName
        self.window = tk.Tk()
        self.__showWindow()

    def __browserFiles(self):
        if(self.txtModuleName.get()==""):
            msg.showerror("Warning","Module name field cannot be empty!")
            self.txtModuleName.config({"background": "Red"})
        else:
            fileName = filedialog.askopenfilename(initialdir ="/",
                                                title ="Select a any python module.",
                                                filetypes = (("Python File","*.py*"),
                                                    ("all files",
                                                    "*.*")))
        
            self.lstModulelist.insert(0,self.txtModuleName.get()+"-"+fileName.split('/')[-1])

            with open (fileName,"r") as pyFile:
                data = pyFile.readlines()

            #project definition
            self.project = objectDefinition.Project(self.__projectName)
            module = parseOperations.ParseModules(fileName.split('/')[-1][0:-3],"\n".join(data)).getModuleObject()
            self.project.addModule(module)
            self.__isAddModule = True
            print("project name--------------------"+self.__projectName)
            print("module name---------------------"+self.txtModuleName.get())

    def __createNetwork(self):
        if(self.__isAddModule):
            ProjectNetwork(self.__networkName,self.project)
            self.window.destroy()
        else:
            msg.showerror("Warning","At least one module must be added to the project to create a network!")
            self.lstModulelist.config(background="Red")

    def __showWindow(self):
        self.frame = tk.Frame(master=self.window, width = 600, height = 300)
        self.frame.pack()

        self.btnAddModule = tk.Button(text = "Add Module",command = self.__browserFiles)
        self.btnAddModule.place(x=100,y=50)

        self.lblModuleList = tk.Label(master=self.frame, text ="Added modules list.")
        self.lblModuleList.place(x=250,y=30)

        self.lblModuleName = tk.Label(master=self.frame, text ="Entry module name")
        self.lblModuleName.place(x=100,y=100)

        self.txtModuleName = tk.Entry()
        self.txtModuleName.place(x=100,y=120)

        self.lstModulelist = tk.Listbox(width =50)
        self.lstModulelist.pack()
        self.lstModulelist.place(x=250,y= 50)

        self.btnNext = tk.Button(text = "Show Network İn Web Browser>",command = self.__createNetwork)
        self.btnNext.place(x=100,y=250)

        self.window.mainloop()