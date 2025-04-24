import tkinter as tk
from tkinter import messagebox, ttk

class ExtractorApplication(tk.Frame):
    TYPE_EXPORT = ['Product', 'Customer', 'Custom']
####################@
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)

        # Manage Radio Button
        self.radioSelected = tk.StringVar()
        self.radioSelected.set( ExtractorApplication.TYPE_EXPORT[0] )

        #Magane Text Label
        self.label_results = None

        self._create_widgets()
        #self._set_default_export_type()
####################@
    def _create_widgets(self):

        """ Create Frame Widgets
            Create the main title label with a large font
            Create a horizontal separator line
            Create radio buttons for each export type
            Create a label to show the selected export type
            Create a button to launch the export
            Create a results label with black background and green text
        """

        ## Title
        title_label = tk.Label(
            self,
            text="Extract All Shopify Data",
            font=("Helvetica", 30),
        ).pack(ipady=5, fill="x")

        line = ttk.Separator(self, orient=tk.HORIZONTAL)
        line.pack(fill="x")

        ## Options

        container = tk.StringVar()
        for export_type in self.TYPE_EXPORT:
            tk.Radiobutton(
                self,

                value=export_type,  # Value Under CONTROL
                text=export_type,   # Texte Under CONTROL

                variable=self.radioSelected,        # Varible to save the value
                command = self.change_export_type,  # Function to call when change

            ).pack(anchor="w", padx=10, pady=5)

        self.label_selected = tk.Label(self)
        self.label_selected.pack(anchor="w", padx=10, pady=5)

        ## Button
        extract_button = tk.Button(self)
        extract_button["text"] = "Launch Extract"
        extract_button["command"] = self.launch_export
        extract_button.pack(side="top")

        ## Show Results
        self.label_results = tk.Text(
            self,
            bg="black",
            fg="green",
            height=100,
            width=50,
        )

        self.label_results.pack(anchor='w', padx=10, pady=5, side="top")

####################@
    def _set_default_export_type(self):
        """Default values
        """
        self.update_label_selected()

####################@
    def update_label_selected(self):
        """Update the selected label.
        """

        selected_value = self.radioSelected.get()
        self.label_selected.config(text=f"Selected : {selected_value}")
    
    def update_label_results(self, text) -> None:
        """Update the results label.
        """

        if (self.label_results != None):
            self.label_results.insert(1.0, text + "\n")
            #new = self.label_results.cget("text") + "\n" + text
            #self.label_results.config(new)

####################@
    def change_export_type(self):
        """Update values in texts labels
        """
        valueNew = self.radioSelected.get()
        print(f'Selected(NEW): {valueNew}')

        self.update_label_selected  ()
        self.update_label_results   (valueNew)

####################@
    def launch_export(self):
        """Launch BTN export
        """
        selected_value = self.radioSelected.get()
        print(f"Launch Export for {selected_value}")

        if selected_value == self.TYPE_EXPORT[0]:
            # Product
            print("Product")

        elif selected_value == self.TYPE_EXPORT[1]:
            # Customer
            print("Customer")

####################@
class Application(tk.Tk):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title('Hello World')
        self.geometry("400x300+50+50")
        self.configure(background="yellow")

root = tk.Tk()
app = ExtractorApplication(root)
app.mainloop()
