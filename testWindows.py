import tkinter as tk
from tkinter import messagebox, ttk

class ExtractorApplication(tk.Frame):
    TYPE_EXPORT = ['Product', 'Customer', 'Custom']

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)

        self._create_widgets()
        self._set_default_export_type()

    def _create_widgets(self):
        ## Title
        title_label = tk.Label(
            self,
            text="Extract All Shopify Data",
            font=("Helvetica", 30),
        ).pack(ipady=5, fill="x")

        line = ttk.Separator(self, orient=tk.HORIZONTAL)
        line.pack(fill="x")

        ## Options

        export_type_var = tk.StringVar()
        for export_type in self.TYPE_EXPORT:
            tk.Radiobutton(
                self,
                variable=export_type_var,
                text=export_type,
                value=export_type,
                command=self.change_export_type,
            ).pack(anchor="w", padx=10, pady=5)

        self.label_selected = tk.Label(self)
        self.label_selected.pack(anchor="w", padx=10, pady=5)

        ## Button
        extract_button = tk.Button(self)
        extract_button["text"] = "Launch Extract"
        extract_button["command"] = self.launch_export
        extract_button.pack(side="top")

        self.label_results = tk.Label(
            self,
            font=("Helvetica", 10),
            anchor='nw',
            background='#000000',
            foreground='#00FF00',
            width=100,
            height=50,
        )
        self.label_results.pack(anchor='w', padx=10, pady=5, side="top")

    def _set_default_export_type(self):
        export_type_var = tk.StringVar()
        export_type_var.set(self.TYPE_EXPORT[0])
        self.export_type_var = export_type_var
        self.update_label_selected()

    def update_label_selected(self):
        selected_value = self.export_type_var.get()
        self.label_selected.config(text=f"Selected: {selected_value}")

    def change_export_type(self, value):
        print(f"Changed Export to {value}")
        self.export_type_var.set(value)
        self.update_label_selected()

    def launch_export(self):
        selected_value = self.export_type_var.get()
        print(f"Launch Export for {selected_value}")

        if selected_value == self.TYPE_EXPORT[0]:
            # Product
            print("Product")

        elif selected_value == self.TYPE_EXPORT[1]:
            # Customer
            print("Customer")


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
