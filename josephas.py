
#josephas program in python
l=[1,2,3,4,5] #numver of peoples in assuming in circle
index=0 #starting person
k=2 #kth person to kill
k=k-1 # decreasing k as we starting from 0 location

#function for killing kth person
def solve(l,k,index):
    if(len(l)==1):
        return l[0]
    else:
        index = (index+k)%len(l) #increating k % size for rotating in circu;lar fashion 
        l.remove(l[index]) #removing kth person
        return solve(l,k,index) #recursive call 
x=solve(l,k,index)
print(x) # printing op
# answer here = 3