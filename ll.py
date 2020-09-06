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
  
def insertAt(head,pos,value):
  newNode = Node(value)
  if pos<0 or pos >length(head):
    return 
  else:
    tail= None
    curr = head
    count =0
    while count<pos:
      count +=1 
      tail = curr
      curr = curr.next
    if tail is None:
      newNode.next = curr
      head = newNode
    else:
      tail.next = newNode
      newNode.next = curr


def length(head):
  count =0
  while head is not None:
    count +=1
    head = head.next
  return count

  
def ithNode(head,pos):
  for i in range(pos):
    head = head.next
  return (head.data)


head = TakeInput()
PrintList(head)
print(ithNode(head,1))
print(ithNode(head,3))
