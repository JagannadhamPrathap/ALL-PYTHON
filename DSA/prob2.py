class Node:
    def __init__(self,val):
        self.val = val
        self.nxt = None
def create(n):
    if n<=0:
        print("Invalid size!")
        return
    head = Node(int(input()))
    current = head
    for i in range(1,n):
        current.nxt = Node(int(input()))
        current = current.nxt
    return head
def mid(head):
    slow = head
    fast = head
    if head is None:
        print("Empty")
        return
    while fast and fast.nxt:
        slow = slow.nxt
        fast = fast.nxt.nxt
    return slow.val
def nth_node(head,y):
    if head is None:
        print("Empty")
        return
    current = head
    c=0
    while current:
        current = current.nxt
        c+=1
    k = c-y
    current = head
    while k:
        current = current.nxt
        k-=1
    return current.val
def display(head):
    current = head
    if not current:
        print("None")
        return
    print(current.val,end='->')
    display(current.nxt)
n = int(input())
head = create(n)
display(head)
print(mid(head))
m = int(input())
print(nth_node(head,m))