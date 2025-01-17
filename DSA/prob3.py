class Node:
    def __init__(self,data):
        self.data = data
        self.nxt = None
def create(n):
    head = Node(int(input()))
    current = head
    if head is None:
        print("None")
        return
    while n!=1:
        current.nxt = Node(int(input()))
        current = current.nxt
        n-=1
    return head
def last(head):
    if head is None:
        print('Empty')
        return
    current = head
    prev = None
    while current.nxt:
        prev = current
        current = current.nxt
    current.nxt = head
    head = current
    prev.nxt = None
    return head
def length(head):
    if head is None:
        print("Empty list")
        return
    current = head
    l = 0
    while current:
        current = current.nxt
        l+=1
    return l
def mid_shift(head):
    slow = head
    fast = head
    prev = None
    while fast and fast.nxt:
        prev = slow
        slow = slow.nxt
        fast = fast.nxt.nxt
    prev.nxt = prev.nxt.nxt
    slow.nxt = head
    head = slow
    return head
def display(head):
    if head is None:
        print("Empty")
        return
    current = head
    while current:
        print(current.data,end='->')
        current = current.nxt
    print('None')
n = int(input())
head = create(n)
display(head)
display(last(head))
display(mid_shift(head))