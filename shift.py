# shifting of number from numbers without changing relative ordering of numbers
def shift(numbers,number):
  i=0
  j=0
  while i<len(numbers):
    if(numbers[i]!=number):
      numbers[j]=numbers[i]
      i+=1
      j+=1
    else:
      i+=1
  while j<len(numbers):
    numbers[j]=number
    j +=1
  return numbers


def main():
  numbers =[int(x) for x in input().split()]
  number = int(input())
  print(shift(numbers,number))

main()
# [3,2,2,2,1,4,2,2] 2
# [3,1,4,2,2,2,2,2] 2


