from Relation import Relation
from Infer import Infer
from Utils import *
import itertools

class Program:
    def __init__(self,KB,I):
        self.KB=KB
        self.I=I
        
    def run(self):
        while(1):
            flag=0
            for j in self.I:
                temp=j.generate(self.KB)
                if temp!=False:
                    if temp not in self.KB:
                        self.KB.append(temp)
                        flag=1
            if(flag==0):
                break
        
    def writeAnswer(self,questions):
        # &: and
        # |: or
        # ~: not
        fo=input('Nhập tên  file output: ')   
        f=open(fo,'w')
        ordinal_number = 0
        for i in questions:
            ordinal_number+=1
            temp=i.split('?-')
            f.write(str(ordinal_number))
            f.write('.')
            f.write(temp[0])
            f.write('\n')
            temp1 = temp[1].split('?')
            q = temp1[-1]
            if len(temp1)>1:
                var = temp1[0:-1]
                temp2=temp1[-1].split('&')
                #Luu ket qua cua tung vi tu
                res_temp=[]
                #Luu cac bien
                temp4 = []
                #Giai ket qua cua tung vi tu
                for k in temp2:
                    check_result1 = True
                    temp3=Relation(k)
                    for x in temp3.getDatas():
                        temp4.append(x)
                    #Luu cac ket qua cua 1 vi tu
                    res_temp1=[]
                    for j in self.KB:
                        if temp3.getName() == j.getName():
                            index =0
                            n = len(temp3.getDatas())
                            while index < n:
                                if temp3.getData(index) in var:
                                    index+=1
                                    continue
                                elif temp3.getData(index) == j.getData(index):
                                    index+=1
                                else:
                                    break
                            if index == n:
                                res_temp1.append(j.getDatas())
                    if len(res_temp1) ==0:
                        check_result1 = False
                        break
                    else:
                        res_temp.append(res_temp1)
                if check_result1 == False:
                     f.write("No result!!!")
                     f.write('\n')
                else:
                    if len(res_temp) >1:
                        check_result2 = False
                        #Ket hop nhung ket qua lai voi nhau tao thanh 1 bo
                        for x in itertools.product(*res_temp):
                            temp5= []
                            for y in x:
                                temp5.extend(y)
                            #Bo nao thoa dieu kien thi ghi ket qua bo do
                            if check(temp5,temp4):
                                check_result2 = True
                                for res_var in var:
                                    index = temp4.index(res_var) 
                                    f.write(res_var +' = ' + temp5[index])
                                    f.write('\t')
                                f.write('\n')
                        if check_result2 == False:
                            f.write("No result!!!")
                            f.write('\n')
                    else:
                        for x in res_temp[0]:
                            if check(x,temp4):
                                for res_var in var:
                                    index = temp4.index(res_var)                
                                    f.write(res_var +' = ' + x[index])
                                    f.write('\t')
                                f.write('\n')
            else:
                s = split_string(q)
                for i in range(len(s)):
                    if s[i] != '&' and s[i] != '|' and s[i] != '[' and s[i] != ']':
                        temp1 = Relation(s[i])
                        res_temp = False
                        for j in self.KB:
                            if temp1 ==j:
                                res_temp=True
                        if res_temp == True:
                            s[i]='1'
                        else:
                            s[i]='0'
                res = eval(''.join(s))
                res_write = ''
                if res == 1:
                    res_write = 'True'
                else:
                    res_write = 'False'
                f.write(res_write)
                f.write('\n')

        print("Xu ly query xong!!!")
        f.close()

    def printKB(self):
        f=open('KB.txt','w')
        for i in self.KB:
            f.write(i.toString())
            f.write('\n')