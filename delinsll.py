class Node:
  def __init__(self,data1,next1=None):
    self.data=data1
    self.next=next1
//converting array to linkedlist
def arrtoll(arr):
  head=Node(arr[0])
  mover=head
  n=len(arr)
  for i in range(1,n):
    temp=Node(arr[i])
    mover.next=temp
    mover=temp
  return head
//delete head of the linked list
def delhead(head):
  if head==None or head.next==None:
    return None
  temp=head
  head=head.next
  del(temp)
  return head
//delete tail of the linkedlist
def deltail(head):
  if head==None or head.next==None:
    return None
  temp=head
  while(temp.next.next!=None):
    temp=temp.next
  mover=temp.next
  temp.next=None
  del(mover)
  return head
//prints entire elements after apply any function
def print_list(head):
  mover=head
  while(mover!=None):
    print(mover.data,end=" ")
    mover=mover.next
// delete kth element from linked list
def delkthel(head,k):
  if head==None: return None
  if k==1:
    head=head.next 
    return head
  c=0
  temp=head
  prev=None
  while(temp!=None):
    c+=1
    if c==k:
      prev.next=prev.next.next 
      del(temp)
      break
    prev=temp
    temp=temp.next
  return head
//delete value element from the linked list
def delvalel(head,val):
  if head==None: return None
  if head.data==val:
    temp=head
    head=head.next
    return head
  temp=head
  prev=None
  while(temp!=None):
    if temp.data==val:
      prev.next=prev.next.next 
      del(temp)
      break
    prev=temp
    temp=temp.next
  return head
//insert head element to the liked list
def inserthead(head,val):
  temp=Node(val,head)
  return temp
//insert tail to the linked list
def inserttail(head, val):
    if head is None:
        return Node(val)
    temp = head
    while temp.next is not None:
        temp = temp.next
    newnode = Node(val)
    temp.next = newnode
    return head
//insert element to certain position in a linked list
def insertpos(head,val,pos):
  if pos==1:
    return Node(val,head)
  c=1
  temp=head
  prev=None
  newnode=Node(val)
  while(temp!=None):
    c+=1
    if c==pos:
      mover=temp.next
      temp.next=newnode
      newnode.next=mover
    temp=temp.next
  return head
arr=[6,9,7,3,2,0]
head=arrtoll(arr)
inspos=insertpos(head,10,8)
print(print_list(inspos))
