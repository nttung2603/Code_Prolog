import itertools
from Relation import Relation
from Utils import *

class Infer:
    #Prolog
    #VD: husband(Person,Wife):-male(Person);married(Person,Wife)
    #left -> right
    def __init__(self,s):
        s=s.split(':-')
        left=s[1].split('&')
        right=s[0]
        self.left=[]
        self.right=Relation(right)
        for i in left:
            temp = Relation(i)
            self.left.append(temp)
        
    def generate(self,KB):
        #Chua cac gia tri của cac bien ben trai co the thay the vao trong infer
        temp = []
        #Chua ten cac bien ben trai
        temp1=[]
        for i in self.left:
            temp1 += i.getDatas()
            #Luu nhung quan he tuong tu voi i
            temp2 = []
            for j in KB:
                if i.isCompatible(j):
                    temp2.append(j.getDatas())
            temp.append(temp2)

        #Intertools.product(temp) tao mang ket hop cac mang trong temp lai voi nhau
        #VD: temp = [[1,2],[3,4]]
        #Intertools.product tra ve [[1,3],[1,4],[2,3],[2,4]]
        for x in itertools.product(*temp):
            temp2=[]
            for i in x:
                temp2 = temp2 + i
            #Xet xem bo x co phu hop voi temp1 hay khong?
            if check(temp2, temp1):
                data = []
                temp3 =  self.right.getDatas()
                for j in temp3:
                    index = temp1.index(j)
                    data.append(temp2[index])
                temp4=Relation("Relation(Data)")
                temp4.setDatas(data)
                temp4.setName(self.right.getName())
                if temp4 in KB:
                    continue
                return temp4
        return False