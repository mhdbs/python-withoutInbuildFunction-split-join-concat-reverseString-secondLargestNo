a = [1,2,3]  
b = [4,5,6]  
c = [7,8,9]

def myFun(*x):  
    s = []
    for i in x:
        s += i
    return s

print myFun(a,b,c)
  