class Table(object):
    def __init__(self,name='',fields=tuple(),tups=None):
        self.__name = name
        self.__fields = fields
        self.__rows = tups        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def fields(self):
        return self.__fields
    @property
    def rows(self):
        return self.__rows
    
    # Relational operations:
    def select(self,field,val):
        result = Table()
        rowList = list()
        for index, fld in enumerate(self.fields):
            if fld == field:
                field = index
        for row in self.rows:
            if row[field] == val:
                rowList.append(row)
        result.name = 'result'
        result.__fields = self.fields
        result.__rows = set(row for row in rowList)
        return result
    def project(self,*fields):
        result = Table()
        indices = list()
        for index, field in enumerate(self.fields):
            if field in fields:
                indices.append(index)
                
        result.name = 'result'
        result.__fields = tuple(field for field in self.fields if field in fields)
                
        result.__rows = {tuple(word for index,word in enumerate(row) if index in indices) for row in self.rows }
        
        return result
    @staticmethod
    def join(tab1,tab2):
        result = Table()
        result.name = "result"  
        result.__fields = tab1.__fields + tab2.__fields
        
        noDuplicates = list() # Remove duplicates but preserve order.
        duplicates = list()
        dup1 = dict()
        dup2 = dict()
        
        for field in result.fields:
            if field not in noDuplicates:
                noDuplicates.append(field)
            else:
                duplicates.append(field)
        result.__fields = tuple(noDuplicates)
        
        for index, field in enumerate(tab1.fields):
            if field in duplicates:
                dup1[field] = index          
        
        for index, field in enumerate(tab2.fields):
            if field in duplicates:
                dup2[field] = index
        
        # first in tuple is row1's index, second is row2's index.       
        pairs = {(value1, value2) for key1, value1 in dup1.items() for key2, value2 in dup2.items() if key1 == key2} 
             
        results = list()
        for row1 in tab1.__rows:
            for row2 in tab2.rows:
                if all(row1[pair[0]] == row2[pair[1]] for pair in pairs): # can join
                    row2 = list(row2)
                    for pair in pairs:
                        row2[pair[1]] = "REMOVE"
                    row2 = [val for val in row2 if val != "REMOVE"]
                    row2 = tuple(row2)
                    results.append(row1 + row2)      
        results = {row for row in results}
        result.__rows = results
        return result
        
    def insert(self,*tup): 
        for row in self.rows:
            if len(row) == len(tup):
                tupList = list()
                tupList.append(tup)
                for row in self.rows:
                    tupList.append(row)
                self.__rows = {row for row in tupList}
                break
            else:
                print "Cannot insert: tuples are not equal in length."
                break
    def remove(self,field,val):
        result = Table()
        for index, fld in enumerate(self.fields):
            if fld == field:
                removeAt = index
        
        self.__rows = {row for row in self.rows for index,word in enumerate(row) if index == removeAt and word != val}
        return self
    
    # Serialization and text backup
    def store(self):
        import pickle
        fname = self.name + ".db"
        with open(fname, 'w') as f:
            pickle.dump(self.name, f)
            pickle.dump(self.fields, f)
            pickle.dump(self.rows, f)
    @staticmethod
    def restore(fname):
        import pickle
        result = Table()
        with open(fname, 'r') as f:
            result.name = pickle.load(f)
            result.__fields = pickle.load(f)
            result.__rows = pickle.load(f)
        return result
    @staticmethod
    def read(fname):
        result = Table()
        with open(fname, "r") as f:
            result.name = (f.readline()).strip() # Using setter.
            result.__fields = tuple(f.readline().strip().split(','))
            result.__rows = {tuple(row.strip().split(',')) for row in f}
        return result     
    def __str__(self):
        toPrint = "%s%s\n" % (self.name, self.fields)
        for x in range(len(self.name)):
            toPrint += '='
        toPrint += "\n"
        for line in self.rows:
            toPrint += "%s\n" % str(line)
        return toPrint
    def write(self,fname):
        fields = ""
        with open(fname, "w") as f:
            print >>f, self.name
            for field in self.fields:
                fields += field + ","
            fields = fields[0:-1]
            print >>f, fields
            for row in self.rows:
                rowPrint = ""
                for word in row:
                    rowPrint += word + ","
                rowPrint = rowPrint[0:-1]
                print >>f, rowPrint