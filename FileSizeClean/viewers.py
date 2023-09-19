import pandas as pd
import tkinter as tk
from tkinter import ttk
# from tkinter import filedialog
def get_input():
    user_input = entry.get()
    result_label.config(text=f'You entered: {user_input}')

class CSVDataGridViewer:
    def __init__(self):
        
       
        self.root = tk.Tk()
        self.root.title("CSV Data Grid View")
        
        entry = tk.Entry(self.root)
        entry.pack()
        def get_input():
            user_input = entry.get()
            result_label.config(text=f'You entered: {user_input}')
        
        result_label = tk.Label(self.root, text="")
        result_label.pack()
        get_input_button = tk.Button(self.root, text="Get Input", command=get_input)
        get_input_button.pack()
        
        # self.load_button.pack()

    def load_csv_in_data_grid(self, file_path):
        

        if file_path:
            df = pd.read_csv(file_path)

            # Create a new tkinter window
            self.data_window = tk.Toplevel(self.root)
            self.data_window.title("CSV Data")

            # Create a Treeview widget to display the data
            self.tree = ttk.Treeview(self.data_window)
            self.tree["columns"] = list(df.columns)

            # Add columns to the Treeview
            for col in df.columns:
                self.tree.column(col, anchor="w", width=100)
                self.tree.heading(col, text=col)

            # Insert data into the Treeview
            for i, row in df.iterrows():
                self.tree.insert("", i, values=list(row))

            # Add a scrollbar
            scrollbar = ttk.Scrollbar(self.data_window, orient="vertical", command=self.tree.yview)
            self.tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side="right", fill="y")

            # Pack the Treeview
            self.tree.pack()

    def run(self):
        self.root.mainloop()

