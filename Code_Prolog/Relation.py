class Relation:
    def __init__(self,s):
        name=""
        data=""

        flag=0
        for i in s:
            if i=='(':
                flag=1
                continue
            if i==')':
                break
            if (flag==0):
                name+=i
            else:
                data+=i               
        self.name=name
        self.data=list(data.split(','))      
    def isKB(self):
        if(self.data[0][0].isupper()):
            return False
        return True
    def getName(self):
        return self.name
    def getDatas(self):
        return self.data
    def getData(self,i):
        return self.data[i]
    def setDatas(self,datas):
        self.data=datas
    def setName(self,name):
        self.name=name
    def isCompatible(self,r):
        if(self.isKB()):
            return False
        if(self.name==r.getName()):
            return True
        return False
    def __eq__(self, other):
        if(other==False):
            return False
        if other.getName()== self.name and other.getDatas()==self.getDatas():
            return True
        return False
    def toString(self):
        data=','.join(self.data)
        return self.name+"("+data+")"