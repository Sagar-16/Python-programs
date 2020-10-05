#Enter The Number For Which You Need To Find The Sum
n = input("Please Enter The Number")
def printNatural(n): #function to print recursively
    if n == 1:      #base case
        print(1,end =' ')
        return
    printNatural(n-1) #calling recursively
    print(n,end =' ') #printing numbers


printNatural(n) #method call
