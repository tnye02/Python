
# imports
import sqlite3

# db connection/creation variable
conn = sqlite3.connect('txt_files.db')

# supplied list of files variable
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# creates the table if it doesn't exist
with conn:
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fileName TEXT \
                )")
    conn.commit()
conn.close()


conn = sqlite3.connect('txt_files.db')
with conn:
    cur = conn.cursor()
    #for loop to iterate through file names
    for files in fileList:
        if files.endswith('.txt'):
            cur.execute("INSERT INTO tbl_txtFiles(col_fileName) VALUES (?)", \
                        (files,))
            print(files)
conn.close()

