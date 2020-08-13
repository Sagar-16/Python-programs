#python program for finding all possible subsets of a string without repetiton.


def m(ip,op):
    if(len(ip) == 0 ):#base case
        if op in hash:#storing in hash table 
            hash[op] += 1
        else:
            hash[op]=1
        return
    else: 
        op1=op
        op2=op
        op2 += str( ip[0])
        ip=ip[1:]  #making input smaller for every call
        m(ip,op1) #recursively calling on new op
        m(ip,op2) #recursively calling on new op2
        return
hash={} # hash table to store generated substring to avoid duplication.
op=" "
ip="abcd"
m(ip,op) #calling function
for k in hash:  #printing all substrings
    if hash[k]==1:
        print(k)
