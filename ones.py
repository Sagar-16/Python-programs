n=3
ones=0
zeros=0
l=[]
op=''
def solve(n,ones,zeros,op):
    if n==0:
        l.append(op)
    if n!=0:
        op2 =op
        op2 += '1'
        solve(n-1,ones+1,zeros,op2)
    if zeros<ones:
        op3 =op
        op3 += '0'
        solve(n-1,ones,zeros+1,op)
solve(n,ones,zeros,op)
for char in l:
    print(char)