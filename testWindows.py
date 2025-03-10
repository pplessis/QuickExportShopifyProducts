import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.create_widgets()

    def create_widgets(self):

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Bonjour Pierre\n(cliquez-moi)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        #self.quit = tk.Button(self, text='Quit', fg='red')
        #self.quit = tk.Button(self, text="QUITTER", fg="red",
        #                      command=self.master.destroy)
        #self.quit.pack(side="bottom")
        self.title = 'TEST'

    def say_hi(self):
        print("Salut tout le monde !")

root = tk.Tk()
root.title('Hello World')
app = Application(root)
app.mainloop()
