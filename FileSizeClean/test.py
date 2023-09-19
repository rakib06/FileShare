import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from threadPool_dir_size import entry_point
import customtkinter
from CTkTable import *


class CSVDataGridViewer:
    def __init__(self):
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        self.root = customtkinter.CTk() 
        self.root.geometry("600x240")
        self.root.title("CSV Data Grid View")
        
        self.load_button = customtkinter.CTkButton(master=self.root, text="Select Folder", command=self.load_csv_in_data_grid)
        self.load_button .place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        # self.load_button.pack()

    def load_csv_in_data_grid(self):
        file_path = filedialog.askdirectory()
        print(file_path)
        csv_file_name = entry_point(file_path)
        if csv_file_name:
            df = pd.read_csv(csv_file_name)
            value = []
            
            v = ['sl']
            v.extend(df.columns)
            value.append(v)
            for i, row in df.iterrows():
                value.append([i]+list(row))
            
            print(value)
                
            table = CTkTable(master=self.root, row=10 if len(value)>10 else len(value) , column=len(value[0]), values=value)
            table.pack(expand=True, fill="both", padx=20, pady=20)
            # Create a new tkinter window
            #self.data_window = customtkinter.CTkLabel(self.root, text="Folder Size ")
            # data_window.title("CSV Data")

            # Create a Treeview widget to display the data
            # self.tree = ttk.Treeview(self.data_window)
            # self.tree["columns"] = list(df.columns)
            
            # Add columns to the Treeview
            # for col in df.columns:
            #     self.tree.column(col, anchor="w", width=100)
            #     self.tree.heading(col, text=col)

            # # Insert data into the Treeview
            # for i, row in df.iterrows():
            #     self.tree.insert("", i, values=list(row))

            # # Add a scrollbar
            # scrollbar = ttk.Scrollbar(self.data_window, orient="vertical", command=self.tree.yview)
            # self.tree.configure(yscroll=scrollbar.set)
            # scrollbar.pack(side="right", fill="y")

            # # Pack the Treeview
            # self.tree.pack()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    csv_viewer = CSVDataGridViewer()
    csv_viewer.run()
