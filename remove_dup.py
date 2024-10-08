import os
import hashlib
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

# Function to find duplicate files
def find_duplicates(directory):
    hashes = defaultdict(list)  # Dictionary to store file hashes and their paths

    # Traverse the directory
    for root, _, files in os.walk(directory):
        for file_name in files:
            # Only process files with the specified extensions
            if file_name.lower().endswith(FILE_TYPES):
                file_path = os.path.join(root, file_name)
                file_hash = get_file_hash(file_path)
                hashes[file_hash].append(file_path)

    # Filter and return duplicates (hashes with more than one file)
    duplicates = {hash_value: file_list for hash_value, file_list in hashes.items() if len(file_list) > 1}
    return duplicates

# Function to delete duplicate files (keeping one)
def delete_duplicates(duplicates):
    for file_list in duplicates.values():
        for file_path in file_list[1:]:  # Keep the first file, delete the rest
            print(f"Deleting: {file_path}")
            os.remove(file_path)

# Main execution
if __name__ == "__main__":
    # Directory to scan
    directory_to_scan = input("Enter the directory to scan for duplicates: ")

    # Find duplicates
    duplicates = find_duplicates(directory_to_scan)

    if duplicates:
        print("Duplicate files found:")
        for hash_value, file_list in duplicates.items():
            print(f"\nFiles with hash {hash_value}:")
            for file_path in file_list:
                print(file_path)

        # Prompt user to delete duplicates
        delete_choice = input("Do you want to delete the duplicates? (yes/no): ").lower()
        if delete_choice == 'yes':
            delete_duplicates(duplicates)
            print("Duplicates deleted.")
        else:
            print("No files were deleted.")
    else:
        print("No duplicate files found.")