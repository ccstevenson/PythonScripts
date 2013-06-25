#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
def view(fname, view_size=25):
    def pageView(page):
        print '[Page %d:]' % page
        f.seek(offsets[page-1])
        for line in range(0, view_size):
            print f.readline(),
        return page
    
    with open(fname, "rb") as f:        
        offsets, line = [0], 1
        while f.readline():
            if line % view_size == 0:
                offsets.append(f.tell())
            line += 1
            
        pageView(1) 
        
        userResponse = 1
        page = 1
        while userResponse != 'q':
            print
            userResponse = raw_input('Command [u,d,t,b,#,q]: ')
            if userResponse == 'u':
                if page-1 > 0:
                    page = pageView(page-1)
                else: page = pageView(len(offsets))
            elif userResponse == 'd' or userResponse == '':
                if page+1 < len(offsets):
                    page = pageView(page+1)
                else: page = pageView(1)
            elif userResponse == 't':
                page = pageView(1)
            elif userResponse == 'b':
                page = pageView(len(offsets))
            elif userResponse.isdigit():
                page = pageView(int(userResponse))
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        view(sys.argv[1])
    elif len(sys.argv) == 3:
        view(sys.argv[1], int(sys.argv[2]))
    else:
        print "Too many/few arguments supplied: view.py takes (1) or (2) arguments."
    