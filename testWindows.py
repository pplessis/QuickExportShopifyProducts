import tkinter as tk
from tkinter import messagebox, ttk

class Application(tk.Frame):
    TYPE_EXPORT = ['Product', 'Customer', 'Custom']

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.defaultValue = Application.TYPE_EXPORT[0]
        self.variable = tk.StringVar(self, f"{self.defaultValue}")
        self.labelSelected  = tk.Label(
                self,
                text=f"Selected: {self.variable.get()}",
            )

        self.variableText = tk.StringVar(self, f'Console')
        self.labelResults = tk.Label (
            self,
            font=("Helvetica", 10),
            anchor='nw',

            background='#000000',
            foreground='#00FF00',
            width='100',
            height='50',

            text= self.variableText.get()
        )


        self.create_widgets()


    def create_widgets(self):
        ## Title
        tk.Label(
            self,
            text="Extract All Shopify Data",
            font=("Font", 30),
            ).pack(ipady=5, fill="x")
        line = ttk.Separator(self, orient=tk.HORIZONTAL)
        line.pack(fill="x")

        ## Options

        for exportType in Application.TYPE_EXPORT:
            tk.Radiobutton(
                self,
                variable    = self.variable,

                text    =   exportType,
                value   =   exportType,

                command =   self.change_export ,
            ).pack(anchor="w", padx=10, pady=5)

        self.labelSelected.pack(anchor="w", padx=10, pady=5)

        ## Button
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Launch Extract"
        self.hi_there["command"] = self.launch_export
        self.hi_there.pack(side="top")


        self.labelResults.pack (anchor='w', padx=10, pady=5 , side='top')

        #self.quit = tk.Button(self, text='Quit', fg='red')
        #self.quit = tk.Button(self, text="QUITTER", fg="red",
        # command=self.master.destroy)
        #self.quit.pack(side="bottom")
        #self.title = 'TEST'

    def change_export (self):
        print( f"Changed Export to {self.variable.get()}")
        self.labelSelected.config ( text=f"Selected: {self.variable.get()}" )

    def launch_export (self):
        selectedValue = self.variable.get()
        print( f"Launch Export for {selectedValue}")

        if (selectedValue == Application.TYPE_EXPORT[0]):
            ## Product
            print( "Product" )

        if (selectedValue == Application.TYPE_EXPORT[1]):
            ## Customer
            print( "Customer" )



root = tk.Tk()
root.title('Hello World')

# Setting some window properties
root.configure(background="yellow")

root.minsize(400, 200)
root.maxsize(450, 500)

root.geometry("400x300+50+50")

app = Application(root)
app.mainloop()
