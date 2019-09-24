import tkinter as tk
from tkinter import ttk
from SimpleSocket import ssocket
#https://docs.python.org/3.3/library/tkinter.html
#https://docs.python.org/3.3/library/tkinter.ttk.html#ttk-widgets ui elements

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, background ='black')
        self.pack()
        self.createWidgets()
        self.sock = ssocket(None)


#setup ui elements/layout
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
        return 65432

        # connect
    def hookup(self):
        portnum = self.getPort()
        host = "127.0.0.1"      #make this real later...
        self.pbar.start(10)
        print("Connecting to port: " + str(portnum))
        self.sock.setupServer(host, portnum)

    def say_hi(self):
        print("hi there, everyone! my way or the highway.")

root = tk.Tk()
root.title('Acme Chat')
root.geometry("300x700")
root.resizable(0, 0)
root.configure(background='black')
app = Application(master=root)
app.mainloop()
