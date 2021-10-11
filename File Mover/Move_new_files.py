import shutil
import os.path
from datetime import date
import datetime
import pathlib
import time


#set where the source of the files are
source = '/Users/tnye0/Desktop/Folder_A/'

#set the destination ppath to Folder B
destination = '/Users/tnye0/Desktop/Folder_B/'


files_list = os.listdir(source)

for i in files_list:
    modTime = time.time() - os.path.getmtime(source+i)
    if modTime > 60*60*24 :
        shutil.move(source+i, destination)
