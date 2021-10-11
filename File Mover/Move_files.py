import shutil
import os.path
import datetime
import pathlib
import time


#set where the source of the files are
source = '/Users/tnye0/Desktop/Folder_A/'

#set the destination ppath to Folder B
destination = '/Users/tnye0/Desktop/Folder_B/'

files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
                                        
    shutil.move(source+i, destination)
