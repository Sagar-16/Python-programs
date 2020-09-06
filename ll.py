#python program of linked list
class Node:
  def __init__(self,data):
    self.data=data
    self.next = None

def PrintList(head):
  cur = head
  while cur:
    print(f"{cur.data} ->",end=" ") 
    cur = cur.next
  print()
   
def TakeInput():
  l =[int(x) for x in input().split()]
  head = None
  tail = None
  for val in l:
    if val == -1:
      break
    newNode = Node(val)
    if head == None:
      head = newNode
      tail = newNode
    else:
      tail.next=newNode
      tail = newNode
  return head
def append(head,data):
  newNode = Node(data)
  tail= head
  while tail.next != None:
    tail= tail.next
  tail.next = newNode
  




head = TakeInput()
PrintList(head)
append(head,10)
append(head,20)
PrintList(head)