

l=[1,2,3,4,5] 
index=0
k=2
k=k-1



def solve(l,k,index):
    if(len(l)==1):
        return l[0]
    else:
        index = (index+k)%len(l)
        l.remove(l[index])
        return solve(l,k,index)
x=solve(l,k,index)
print(x)