# two number pair sum problem using hashing
#tc - O(n)
#sc -O(n)

hash={}
for i in range(1000):
  hash[i]=0


l=[1,2,3,4,5,6,7,9,10]
sum =8


def findPair(l,sum):
  for i in range(len(l)):
    temp = sum - l[i]
    if(temp in hash):
      print(f"{l[i]} {temp}")
    else:
      hash[l[i]]=1

findPair(l,sum)