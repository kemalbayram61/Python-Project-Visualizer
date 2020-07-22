import tkinter as tk
import tkinter.messagebox as msg
from addModuleScreen import AddModuleScreen

class NamingScreen:
    #variables for naming screen
    __projectName =""
    __networkName = ""
    
    def __init__(self):
        self.window = tk.Tk()
        self.__showWindow()

    def __clickNextButton(self):
        if(self.txtProjectName.get() == "" or self.txtNetworkName.get() == ""):
            msg.showerror("Warning","Project name and Network name field cannot be empty!")
            self.txtProjectName.config({"background": "Red"})
            self.txtNetworkName.config({"background": "Red"})
        else:
            self.__projectName = self.txtProjectName.get()
            self.__networkName = self.txtNetworkName.get() 
            self.window.destroy()
            AddModuleScreen(self.__projectName,self.__networkName)

    def __showWindow(self):
        self.frame = tk.Frame(master=self.window, width = 600, height = 300)
        self.frame.pack()

        self.lblProjectName = tk.Label(master=self.frame, text ="Enter the project name.")
        self.lblProjectName.place(x=100,y=50)

        self.lblNetworkName = tk.Label(master=self.frame, text="Enter the network name.")
        self.lblNetworkName.place(x=100,y=120)

        self.txtProjectName = tk.Entry()
        self.txtProjectName.place(x=100,y=80)


        self.txtNetworkName = tk.Entry()
        self.txtNetworkName.place(x=100,y=150)

        self.btnNext = tk.Button(text = "Next>",command = self.__clickNextButton)
        self.btnNext.place(x=100,y=250)

        self.window.mainloop()

NamingScreen()
