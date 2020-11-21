from Relation import Relation
from Infer import Infer
from utils import split_string
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
        # ^: and
        # v: or
        # ~: not
        f=open('result_query.txt','w')
        for i in questions:
            temp=i.split('-')
            f.write(temp[0])
            f.write('\n')
            if 'X' in temp[1]:
                temp1=Relation(temp[1])
                for j in self.KB:
                    if temp1.getName()==j.getName():
                        k =0
                        n = len(temp1.getDatas())
                        count =0
                        while k < n:
                            if temp1.getData(k) == j.getData(k):
                                count+=1
                            k+=1
                        if count == n-1:
                            f.write(j.toString())
                            f.write('\n')
            else:
                s = split_string(temp[1])
                for i in range(len(s)):
                    if s[i] != '^' and s[i] != 'v' and s[i] != '[' and s[i] != ']':
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
                    elif s[i] == '^':
                        s[i]='&'
                    elif s[i] == 'v':
                        s[i] = '|'
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
            f.write(i.getName())
            f.write(",")
            listToStr = ' '.join(map(str, i.getDatas()))
            f.write(listToStr)
            f.write('\n')

#Doc file input
#fp=input('Nhập tên  file input: ')            
f=open('hoang_gia_anh.txt','r')
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
f=open('query.txt','r')
f2=f.read().splitlines()
for x in f2:
    questions.append(x)

main=Main(KB,I)
main.run()
main.printKB()
main.writeAnswer(questions)