def readfiles(directory):
    import sqlite3, os
    conn = sqlite3.connect('filesdb')
    cur = conn.cursor()
    cur.execute('create table files(ext text, path text, fname text)')    
    for root, directories, files in os.walk(directory): # Eliminates need to check os.path.isfile(f)
        for f in files:
            filename, extension = os.path.splitext(f)
            if extension == "":
                extension = None
            if f[0:1] != '.': 
                cur.execute('insert into files values (?,?,?)',(extension,root,f))
    query = '''select * from files'''
    data = cur.execute(query)
    with open('files.txt', 'w') as f:
        for row in data: print>>f, row   
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        readfiles(sys.argv[1])
    else:
        print "Too many/few arguments supplied: readfiles.py takes (1) argument."