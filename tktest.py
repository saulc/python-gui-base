import tkinter as tk
from tkinter import ttk
#https://docs.python.org/3.3/library/tkinter.html
#https://docs.python.org/3.3/library/tkinter.ttk.html#ttk-widgets ui elements

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, background ='black')
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.connect = tk.Button(self)
        self.connect.configure(background='black')
        self.connect["text"] = "Connect"
        self.connect["command"] = self.hookup
        self.connect.pack( fill = tk.X)

        self.pbar =  ttk.Progressbar(self, orient="horizontal", length=260, mode="determinate") 
        self.pbar.pack( fill = tk.X)

        self.option = tk.Button(self)
        self.option.configure(background='black')
        self.option["text"] = "Options"
        self.option["command"] = self.say_hi
        self.option.pack( fill = tk.X)

        self.QUIT = tk.Button(self, text="QUIT", bg='black' ,fg="red", command=root.destroy)
        self.QUIT.pack( fill = tk.X)

    def getPort(self):
        return 4444

    def hookup(self):
        portnum = self.getPort()
        self.pbar.start(10)
        print("Connecting to port: " + str(portnum))

    def say_hi(self):
        print("hi there, everyone! my way or the highway.")

root = tk.Tk()
root.title('Acme Chat') 
root.geometry("300x700")  
root.resizable(0, 0) 
root.configure(background='black')
app = Application(master=root)
app.mainloop()