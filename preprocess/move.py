import os
import shutil

# define the source directory and destination directory
src_dir = './layer3_text'
dst_dir = './files2'

# walk through the source directory and its subdirectories
for root, dirs, files in os.walk(src_dir):
    for file in files:
        # get the full path of the current file
        file_path = os.path.join(root, file)
        
        # create the destination directory if it doesn't exist
        os.makedirs(dst_dir, exist_ok=True)
        
        # copy the file to the destination directory
        shutil.copy2(file_path, dst_dir)
