#python program for 0-1 knapsack using recursion 


weights=[1,3,6,7,10]  # weights array for items
values=[2,4,7,9,12]   # values array for items
n=5                    #number of items
w=10                   #bags weight 
def knapsack(weights,values,w,n):
	if n==0 or w ==0:  #base case
		return 0
	if weights[n-1]<=w:  #if last items weight less than bags weight
		return max((values[n-1]+ knapsack(weights,values,w-weights[n-1],n-1)),(knapsack(weights,values,w,n-1)))
	if weights[n-1]>w: #  if last items weight more than bags weight
		return knapsack(weights,values,w,n-1)


result = knapsack(weights,values,w,n)
print(result)  #printing result
#13
