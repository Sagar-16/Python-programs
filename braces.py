def braces(open,close,op):
    if open == 0 and close == 0:
        l.append(op)
    if open !=0:
        op1 = op
        op += '('
        braces(open-1,close,op1)
    if close > open:
        op2 =op
        op2 += ')'
        braces(open,close-1,op)





l=[]#list to store balanced paranthesis
n=3 #take input from user
open = n
close = n
op ="" #to store output
braces(open,close,op)
