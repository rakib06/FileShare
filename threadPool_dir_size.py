import os
import concurrent.futures
from pathlib import Path
import csv
from datetime import datetime

def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    bytess = total_size
    resMB, resGB = bytess // 1000 // 1000, bytess // 1000 // 1000 / 1000
    print(f"{start_path}\t ==>\t \t{resMB} MB, {resGB} GB")

    return start_path, resMB, resGB

def process_folders(path_list):
   
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(get_size, path_list))

    # Generate a dynamic CSV file name using a timestamp
    folder,_ =  os.path.split(path_list[0])
    folder = folder.replace("\\","~").replace(":", "~")
    print(folder)
   
    
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    csv_file_name = f'folder_sizes_of_{folder}_{timestamp}.csv'

    # Write the results to the CSV file
    with open(csv_file_name, mode='w', newline='') as csv_file:
        fieldnames = ['Folder', 'Size (MB)', 'Size (GB)']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in sorted(results, key=lambda x: x[1], reverse=True):
            writer.writerow({'Folder': result[0], 'Size (MB)': result[1], 'Size (GB)': result[2]})

ip = input("Path: ").lstrip()
p = Path(ip)

# All subdirectories in the current directory, not recursive.
path_list = [f for f in p.iterdir() if f.is_dir()]

process_folders(path_list)
