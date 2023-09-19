import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from threadPool_dir_size import entry_point

class CSVDataGridViewer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CSV Data Grid View")
        
        self.load_button = tk.Button(self.root, text="Select Folder", command=self.load_csv_in_data_grid)
        self.load_button.pack()

    def load_csv_in_data_grid(self):
        file_path = filedialog.askdirectory()
        print(file_path)
        csv_file_name = entry_point(file_path)
        if csv_file_name:
            df = pd.read_csv(csv_file_name)

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

if __name__ == "__main__":
    csv_viewer = CSVDataGridViewer()
    csv_viewer.run()
