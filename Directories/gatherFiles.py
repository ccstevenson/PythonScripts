def gatherfiles(db, extensions):
    import zipfile, sqlite3   
    
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    for extension in extensions:
        query = '''select path,fname from files where ext=?'''
        data = cur.execute(query, ['.' + extension])
        zfile = zipfile.ZipFile(extension + '.zip', 'w')
        for row in data:
            filename = row[1]
            path = row[0] + '\\' + row[1]
            zfile.write(path)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 3:
        db = (sys.argv[1])
        extensions = (argument for index, argument in enumerate(sys.argv) if index > 1)
        gatherfiles(db, extensions)
    else:
        print "Too few arguments supplied: gatherfiles.py takes (2) or more arguments."