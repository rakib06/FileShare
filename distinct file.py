import os
import hashlib
import shutil
from collections import defaultdict

# Define file types to consider
FILE_TYPES = ('.pptx', '.doc', '.pdf', '.zip')

# Function to calculate hash of a file
def get_file_hash(file_path, hash_algo=hashlib.md5):
    hash_obj = hash_algo()
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# Function to find unique files (distinct files based on hash)
def find_unique_files(directory, exclude_directory):
    hashes = defaultdict(list)  # Dictionary to store file hashes and their paths

    # Traverse the directory, excluding the destination directory
    for root, _, files in os.walk(directory):
        # Skip the exclude_directory (destination) during the scan
        if exclude_directory and os.path.commonpath([root, exclude_directory]) == exclude_directory:
            continue
        
        for file_name in files:
            # Only process files with the specified extensions
            if file_name.lower().endswith(FILE_TYPES):
                file_path = os.path.join(root, file_name)
                file_hash = get_file_hash(file_path)
                hashes[file_hash].append(file_path)

    # Return one file per hash (unique files)
    unique_files = {hash_value: file_list[0] for hash_value, file_list in hashes.items()}
    return unique_files

# Function to copy distinct files to a new directory
def copy_unique_files(unique_files, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)  # Create directory if it doesn't exist
    
    for file_path in unique_files.values():
        # Copy each unique file to the destination directory
        file_name = os.path.basename(file_path)  # Get the base file name
        destination_path = os.path.join(destination_directory, file_name)
        print(f"Copying {file_path} to {destination_path}")
        shutil.copy2(file_path, destination_path)  # Copy the file with metadata

# Main execution
if __name__ == "__main__":
    # Directory to scan for duplicates
    directory_to_scan = input("Enter the directory to scan for duplicates: ")

    # Destination directory for unique files
    destination_directory = input("Enter the directory to copy distinct files to: ")

    # Find unique files, excluding the destination directory
    unique_files = find_unique_files(directory_to_scan, destination_directory)

    if unique_files:
        print("Copying unique files to the destination directory...")
        copy_unique_files(unique_files, destination_directory)
        print("All unique files have been copied.")
    else:
        print("No unique files found.")