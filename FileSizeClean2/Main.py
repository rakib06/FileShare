"""
Example script for testing the Azure ttk theme
Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""
from tkinter import filedialog
from threadPool_dir_size import process

import tkinter as tk
from tkinter import ttk
from csv_read import get_data, get_data_with_SL, get_data_with_GridFormat
import os
from tkinter import messagebox

class App(ttk.Frame):
    def __init__(self, parent):
        global istreeSetup, CURRENT_FOLDER 
        istreeSetup = False
        CURRENT_FOLDER = None
        
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Create control variables
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=2)
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value=75.0)

        # Create widgets :)
        self.setup_widgets()

    def setup_widgets(self):
        self.check_frame = ttk.LabelFrame(self, text="Checkbuttons", padding=(20, 10))
        self.check_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        def askDir():
            global istreeSetup, CURRENT_FOLDER
            folder_path = filedialog.askdirectory()
            print(folder_path)
            startprocess_csv(folder_path)
            CURRENT_FOLDER = folder_path    
        
        def startprocess_csv(folder_path):
            
            csv_file = process(folder_path)
            data = get_data_with_GridFormat(csv_file_name=csv_file)
            if not istreeSetup:
                setupTree()
            treeview(treeview_data=data)
            
            
        def backProcess():
            
            global CURRENT_FOLDER
            if CURRENT_FOLDER is not None:
                CURRENT_FOLDER = os.path.dirname(CURRENT_FOLDER)
                startprocess_csv(CURRENT_FOLDER) 
        
        # Button
        self.button = ttk.Button(self.check_frame, text="Add Folder", command=askDir)
        # self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")
        self.button.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
        
        # Back
        self.button = ttk.Button(self.check_frame, text="Back", command=backProcess)
        # self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")
        self.button.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        
        
        def setupTree():
            global istreeSetup
            
            # Pane #1
            self.pane_1 = ttk.Frame(self.paned, padding=5)
            self.paned.add(self.pane_1, weight=1)
        
            # Scrollbar
            self.scrollbar = ttk.Scrollbar(self.pane_1)
            self.scrollbar.pack(side="right", fill="y")
            self.pane_1 = ttk.Frame(self.paned, padding=5)
            self.paned.add(self.pane_1, weight=1)
            # Treeview
            self.treeview = ttk.Treeview(
                self.pane_1,
                selectmode="extended",
                yscrollcommand=self.scrollbar.set,
                columns=(1, 2),
                height=10,
                #show="headings"
            )
            self.treeview.pack(expand=True, fill="both")
            self.scrollbar.config(command=self.treeview.yview)

            # Treeview columns
            self.treeview.column("#0", anchor="w", width=320)
            self.treeview.column(1, anchor="w", width=80)
            self.treeview.column(2, anchor="w", width=80)
            
            # Treeview headings
            self.treeview.heading("#0", text="Folder Path", anchor="center")
            self.treeview.heading(1, text="Size-MB", anchor="center")
            self.treeview.heading(2, text="Size-GB", anchor="center")
               
            
            istreeSetup = True
            
        def treeview(treeview_data):
            for i in self.treeview.get_children():
                self.treeview.delete(i)
            
            # Insert treeview data
            for item in treeview_data[1:]:
                self.treeview.insert(
                parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
                )
                # if item[0] == "" or item[1] in {8, 21}:
                #     self.treeview.item(item[1],  open=False)  # Open parents


            # Select and scroll
            self.treeview.selection_set(10 if len(treeview_data)> 10 else len(treeview_data[1:]))
            self.treeview.see(7 if len(treeview_data)> 7 else len(treeview_data[1:]))
            def on_item_click(event):
                item = self.treeview.selection()[0]
                dir_ = self.treeview.item(item)['text']
                # name, value = self.treeview.item(item, 'text')
                # print(f"Clicked on {name}: {value}")
                print(dir_)
                result = messagebox.askyesno("Confirmation", f"Are you sure you want to start the process for {dir_}?")
                if result: startprocess_csv(dir_)

            # Bind the click event to the Treeview
            self.treeview.bind("<ButtonRelease-1>", on_item_click)
            
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

        # Notebook, pane #2
        self.pane_2 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_2, weight=3)

        # Notebook, pane #2
        self.notebook = ttk.Notebook(self.pane_2)
        self.notebook.pack(fill="both", expand=True)

        # Tab #1
        self.tab_1 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_1.columnconfigure(index=index, weight=1)
            self.tab_1.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_1, text="Tab 1")

       
        # Label
        self.label = ttk.Label(
            self.tab_1,
            text="Folder Size Check - 1789",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=1, column=0, pady=10, columnspan=2)

        

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("")

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()
