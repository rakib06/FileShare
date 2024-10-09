import os
import zipfile
import py7zr
import logging
from datetime import datetime

# Set up logging with a dynamic filename based on the current date and time
log_filename = datetime.now().strftime('extract_log_%Y%m%d_%H%M%S.log')
logging.basicConfig(filename=log_filename, 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def extract_archives_in_directory(directory):
    # Iterate over all files in the directory
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            
            # Check if the file is a .zip file
            if filename.endswith('.zip'):
                extraction_path = os.path.join(foldername, filename.replace('.zip', ''))
                os.makedirs(extraction_path, exist_ok=True)
                try:
                    # Unzip the file
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(extraction_path)
                    logging.info(f'Unzipped: {filename} into {extraction_path}')
                    print(f'Unzipped: {filename} into {extraction_path}')
                except Exception as e:
                    logging.error(f'Failed to unzip: {filename} - Error: {e}')
            
            # Check if the file is a .7z file
            elif filename.endswith('.7z'):
                extraction_path = os.path.join(foldername, filename.replace('.7z', ''))
                os.makedirs(extraction_path, exist_ok=True)
                try:
                    # Extract the .7z file
                    with py7zr.SevenZipFile(file_path, mode='r') as z:
                        z.extractall(extraction_path)
                    logging.info(f'Extracted: {filename} into {extraction_path}')
                    print(f'Extracted: {filename} into {extraction_path}')
                except Exception as e:
                    logging.error(f'Failed to extract: {filename} - Error: {e}')

# Specify the directory containing the archive files
directory = 'C:/path/to/your/directory'

# Call the function
extract_archives_in_directory(directory)