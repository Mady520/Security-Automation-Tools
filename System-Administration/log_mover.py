# This one is an automation script which will be used to move log file form a particular folder to anohter one with the files at least 7 days older 

import os 
import shutil
from datetime import datetime

source_dir = ""
dest_dir = "" 
if not os.path.exists(source_dir):
    print(f"ERROR :The source directory {source_dir} does not exists")
    exit()

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
    print(f"Created destination directory {dest_dir}")

now = datetime.now()
for filename in os.listdir(source_dir):
    filepath = os.path.join(source_dir ,filename)

    if os.path.isfile(filepath) and filename.endswith(".log"):
       try:
        file_mtime = datetime.fromtimestamp(os.path.getmtime(filepath))
    
        if (now - file_mtime).days > 7:
            dest_path = os.path.join(dest_dir, filename)

            if os.path.exists(dest_path):
               print(f"filename {filename} already exists in the folder. Skipping!")
               continue

            shutil.move(filepath, dest_path)
            print(f"Successfully moved {filename}")
       except PermissionError:
            print(f"Permission denied: Cannot move {filename}. Are you running as root/admin?")
       except Exception as e:
            print(f"An error occurred with {filename}: {e}")

            
