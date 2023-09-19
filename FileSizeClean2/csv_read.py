import pandas as pd

def get_data(csv_file_name):
    # file_path = filedialog.askdirectory()
    # print(file_path)
    # csv_file_name = entry_point(file_path)
    if csv_file_name:
        df = pd.read_csv(csv_file_name)
        value = []
        
       
        value.append(df.columns)
        for i, row in df.iterrows():
            value.append(list(row))
        
        print(value)
            
        return value

def get_data_with_SL(csv_file_name):
    # file_path = filedialog.askdirectory()
    # print(file_path)
    # csv_file_name = entry_point(file_path)
    if csv_file_name:
        df = pd.read_csv(csv_file_name)
        value = []
        
        v = ['sl']
        v.extend(df.columns)
        value.append(v)
        for i, row in df.iterrows():
            value.append([i+1]+list(row))
        
        print(value)
            
        return value

# ("", 1, "Parent", ("Item 1", "Value 1")),
def get_data_with_GridFormat(csv_file_name):
    # file_path = filedialog.askdirectory()
    # print(file_path)
    # csv_file_name = entry_point(file_path)
    if csv_file_name:
        df = pd.read_csv(csv_file_name)
        value = []
        
        v = ['sl']
        v.extend(df.columns)
        value.append(v)
        for i, row in df.iterrows():
            val = ("", i+1, row[0], list(row[1:]) )
            value.append(val)
        
        print(value)
            
        return value