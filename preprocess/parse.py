import os
from parse2 import wikimedia_citation_to_raw_text as convert

src_dir = './files2'

for root, dirs, files in os.walk(src_dir):
    for file in files:
        # get the full path of the current file
        file_path = os.path.join(root, file)
        
        # open the file and read its contents
        with open(file_path, 'r', encoding="utf8") as f:
            file_contents = f.read()
        
        plain_text = convert(file_contents)
        
        with open(file_path, 'w', encoding="utf8") as f:
            f.write(plain_text)
