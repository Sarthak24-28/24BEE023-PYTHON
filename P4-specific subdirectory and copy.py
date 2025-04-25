import os
import shutil

source_file_path = ""        
destination_dir = ""       

os.makedirs(destination_dir, exist_ok=True)

shutil.copy(source_file_path, destination_dir)

print("File copied from source path to destination path")
