class Node:
    def __init__(self,val):
        self.val = val
        self.nxt = None
def create(n):
    if n<=0:
        print("Invalid input..!")
        return
    head = Node(int(input()))
    current = head
    for i in range(1,n):
        current.nxt = Node(int(input()))
        current = current.nxt
    return head
def check(head1,head2):
    if head1 is None or head2 is None:
        print("Empty lists")
        return
    current1 = head1
    current2 = head2
    flag = True
    while current1 and current2:
        if current1.val != current2.val:
            flag = False
            break
        current1 = current1.nxt
        current2 = current2.nxt

    if not flag:
        print("Not identical")
    else:
        print("Identical")
def display(head):
    current = head
    if current is None:
        print("None")
        return
    print(current.val,end='->')
    display(current.nxt)
n = int(input())
head1 = create(n)
head2 = create(n)
display(head1)
display(head2)
check(head1,head2)