from Relation import Relation
from Infer import Infer
from utils import *
import itertools

class Main:
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
        f=open('result_query4.txt','w')
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
            if len(temp[1:])>1:
                var = temp1[0:-1]
                temp2=temp1[-1].split('&')
                #Luu ket qua cua tung vi tu
                res_temp=[]
                #Luu cac bien
                temp4 = []
                for k in temp2:
                    check_result1 = True
                    temp3=Relation(k)
                    for x in temp3.getDatas():
                        temp4.append(x)
                    #Luu ket qua cua 1 vi tu
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
                        for x in itertools.product(*res_temp):
                            temp5= []
                            for y in x:
                                temp5.extend(y)
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
                            if temp1.getName() == j.getName():
                                k =0
                                n = len(temp1.getDatas())
                                while k < n:
                                    if temp1.getData(k) == j.getData(k):
                                        k+=1
                                    else:
                                        break
                                if k == n:
                                    res_temp = True
                                    break
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
        f=open('test1.txt','w')
        for i in self.KB:
            f.write(i.toString())
            f.write('\n')

#Doc file input
#fp=input('Nhập tên  file input: ')            
#f=open('hoang_gia_anh.txt','r')
f=open('test1.txt','r')
f1=f.read().splitlines()
KB=[]
I=[]
flag = 0
for x in f1:
    if x=='*':
        flag+=1
        continue
    if flag == 0:
        temp=Relation(x)
        KB.append(temp)
    elif flag == 1:
        temp=Infer(x)
        I.append(temp)
f.close()

#Doc file query
questions=[]
f=open('query3.txt','r')
f2=f.read().splitlines()
for x in f2:
    questions.append(x)

main=Main(KB,I)
main.run()
main.printKB()
main.writeAnswer(questions)