def split_string(expression):
    start = 0
    end =0
    list = []
    while end < len(expression):
        #Kiem tra ki tu do phai la toan tu khong
        if expression[end] =='&' or expression[end] =='|':
            list.append(expression[start:end])
            list.append(expression[end:end+1])
            start = end+1
        #Kiem tra ki tu do phai la '[' khong
        if expression[end] == '[':
            list.append(expression[start:end+1])
            start = end + 1
        #Kiem tra ki tu do phai la ']' khong
        if expression[end] == ']':
            list.append(expression[start:end])
            start = end
        end+=1
    if start < end:
        list.append(expression[start:end])
    return list

def my_hash(x):
    temp=[]
    n=len(x)
    for i in range(0,n):
        temp.append(i)
    i=n-1
    while(i>=0):
        j=i
        while(j>=0):
            if(x[j]==x[i]):
                temp[i]=j
            j=j-1
        i=i-1
    return temp

def check(x,y):
    #Ta se chuyen x ve dang so de de so sanh
    #VD: [A,B,A] -> [0,1,0]
    if my_hash(x) == my_hash(y):
        return True
    return False