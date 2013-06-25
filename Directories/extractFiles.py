def extractfiles(zipf, regex):
    import zipfile, os, re
    zfile = zipfile.ZipFile(zipf, "r")
    
    for f in zfile.namelist(): # Using the file list circumvents the underscore problem.
        if  re.match(regex, os.path.basename(f)):
            zfile.extract(f, 'extractfilesresult') # Extracting to special directory to ensure correctness.
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        extractfiles(sys.argv[1], sys.argv[2])
    else:
        print "Too many/few arguments supplied: extractfiles.py takes (2) arguments."