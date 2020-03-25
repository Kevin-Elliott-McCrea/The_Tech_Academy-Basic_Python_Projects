
import sqlite3

conn = sqlite3.connect('basicPythonSQL.db')
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
cur = conn.cursor()


with conn:
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_textFiles(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    conn.commit()

    for i in fileList:
        if i.endswith('.txt'):
            cur.execute('INSERT INTO tbl_textFiles (file_name) VALUES (?)', (i,))
        conn.commit()

    cur.execute("SELECT * FROM tbl_textFiles")
    result = cur.fetchall()
    print('\nThese are the file names ending in .txt: ' + str(result))
conn.close()
