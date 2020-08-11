#python programs to generate balanced paranthesis

def braces(open,close,op):
    if open == 0 and close == 0:
        l.append(op)
    if open !=0:
        op1 = op
        op1 += '('
        braces(open-1,close,op1)
    if close > open:
        op2 =op
        op2 += ')'
        braces(open,close-1,op2)

l=[]#list to store balanced paranthesis
n=3 #take input from user
open = n
close = n
op ="" #to store output
braces(open,close,op)


for char in l:
    print(char)


#output:
((()))
(()())
(())()
()(())
()()()

