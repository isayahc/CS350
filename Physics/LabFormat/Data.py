"""Goal: Make an object that takes the shape of a table
    inputs: (1)a list of attributes
    (2) the number of objects
    """

class Data:
    def __init__(self, columns, n):
        self.columns = columns
        self.n = n

    def listofdicts(self):
        """returns a list of dictionary objects"""
        objlist = list()
        for x in range(1,self.n):
            obj = {i : input("please input {} for row {}: ".format(i,x)) for i in self.columns}
            objlist.append(obj)
            print(x)
        return objlist
        
    def savetotext(self,f):
        """creates a new file to store info"""
        f = open(f,'w')
        f.write(self.listofdicts().__str__())
        f.close()

    def savedtext(self,f):
        f = open(f,'r')
        f.readline()
        f.close()
    


        
    def __str__(self):
        pass
        




w = Data(['name','Temperature','Pressure'],6)
#w.listofdicts()
w.savetotext("testfile1.txt")
