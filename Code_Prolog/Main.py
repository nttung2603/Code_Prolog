from Program import Program
from Relation import Relation
from Infer import Infer
#Doc file input
fp=input('Nhập tên  file input: ')            
f=open(fp,'r')
f1=f.read().splitlines()
KB=[]
I=[]
questions=[]
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
    else:
        questions.append(x)
f.close()

main=Program(KB,I)
main.run()
#main.printKB()
main.writeAnswer(questions)