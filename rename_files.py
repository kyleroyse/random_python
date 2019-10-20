import os
def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir("/Users/kyleroyse/Downloads/prank/")
    print (file_list)
    saved_path = os.getcwd()
    print("The current working directory is "+ saved_path)
    os.chdir("/Users/kyleroyse/Downloads/prank/")
    
    # (2) for each file, rename the filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate({ord(c):""for c in "0123456789"}))
    os.chdir(saved_path)
    
rename_files()
