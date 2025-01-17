class Node:
    def __init__(self,data):
        self.data = data
        self.nxt = None
def create(n):
    if n<0:
        print("Invalid input!")
        return
    head = Node(int(input()))
    current = head
    for i in range(1,n):
        current.nxt = Node(int(input()))
        current = current.nxt
    return head
def delete_alter(head):
    if head is None:
        return head
    current = head.nxt
    prev = head
    while current:
        prev.nxt = current.nxt
        current.nxt = None
        prev = prev.nxt
        current = prev.nxt
    return head
def display(head):
    if head is None:
        print("Empty")
        return
    current = head
    while current:
        print(current.data,end = '->')
        current = current.nxt
    print('None')
n = int(input())
head = create(n)
display(head)
display(delete_alter(head))
