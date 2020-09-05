#Stack program using list in python


class stack:
  def __init__(self):
    self.l=[]

  def add(self,data):
    self.l.append(data)


  def Pop(self):
    if(len(self.l)==0):
      print("List is empty.")
    else:
      x = self.l[-1]
      self.l.pop()
      print(f"{x} is removed")


  def show(self):
    if (len(self.l)==0):
      print("list is empty")
    else:
      for i in range(len(self.l)):
        print(self.l[i],end=" ")
      print()

  
    
  def peek(self):
    if(len(self.l)==0):
      print("Stack is empty")
    else:
      return self.l[-1]
  def isempty(self):
    return len(self.l)==0

  

def main():
  s = stack()
  while(True):
    print('''1.add
2.remove
3.top element
4.isempty
5.display
6.exit
    ''')
    choice = int(input())
    if (choice == 1):
      data = int(input("Enter data : "))
      s.add(data)
    elif (choice == 2 ):
      s.Pop()
    elif(choice == 3):
      print(s.peek())
    elif(choice == 4):
      if(s.isempty()):
        print("yes")
      else:
        print("NO")
    elif(choice == 5):
      s.show()
    elif (choice == 6):
      exit(0)
    else:
      print ("Invalid choice")




main()