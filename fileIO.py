

import os
import time
import fnmatch

# declare variables for path
path = "C:\\python_projects\\"

file_name_array = os.listdir(path)


for files in file_name_array:
    full_path = os.path.join(path, files)
    mTime = os.path.getmtime(full_path)
    cTime = time.ctime(mTime)
    ext = '.txt'
    fileExt = os.path.splitext(full_path)
    if ext in fileExt:
        print('{} - Modified: {}'.format(full_path, cTime))

