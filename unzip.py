import os
import zipfile
import py7zr

# Function to unzip all .zip and .7z files in the directory
def extract_archives_in_directory(directory):
    # Iterate over all files in the directory
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            
            # Check if the file is a .zip file
            if filename.endswith('.zip'):
                extraction_path = os.path.join(foldername, filename.replace('.zip', ''))
                os.makedirs(extraction_path, exist_ok=True)
                # Unzip the file
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(extraction_path)
                print(f'Unzipped: {filename} into {extraction_path}')
            
            # Check if the file is a .7z file
            elif filename.endswith('.7z'):
                extraction_path = os.path.join(foldername, filename.replace('.7z', ''))
                os.makedirs(extraction_path, exist_ok=True)
                # Extract the .7z file
                with py7zr.SevenZipFile(file_path, mode='r') as z:
                    z.extractall(extraction_path)
                print(f'Extracted: {filename} into {extraction_path}')

# Specify the directory containing the archive files
directory = '/path/to/your/directory'

# Call the function
extract_archives_in_directory(directory)