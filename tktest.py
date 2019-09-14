import tkinter as tk

#https://docs.python.org/3.3/library/tkinter.html

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Options"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.title('Acme Chat') 
root.geometry("300x700")  
root.resizable(0, 0) 
app = Application(master=root)
app.mainloop()