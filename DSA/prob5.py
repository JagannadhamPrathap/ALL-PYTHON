class Node:
    def __init__(self,data):
        self.data = data
        self.nxt = None
def create(n):
    if n<=0:
        print("Invalid input")
        return
    head = Node(int(input()))
    current = head
    while n>1:
        current.nxt = Node(int(input()))
        current = current.nxt
        n-=1
    return head
def rev(head):
    current = head
    prev = None
    while current:
        temp = current.nxt
        current.nxt = prev
        prev = current
        current = temp
    return prev
def add1(head):
    head = rev(head)
    current = head
    last = None
    c=1
    while current:
        x = c + current.data
        c = 1 if x>=10 else 0
        current.data = x%10
        last = current
        current = current.nxt
    if c>0:
        last.nxt = Node(c)
    return rev(head)
def display(head):
    if head is None:
        print("Empty list")
        return
    current = head
    while current:
        print(current.data,end='->')
        current = current.nxt
    print("None")
n = int(input())
head = create(n)
display(head)
display(add1(head))