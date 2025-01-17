class Node:
    def __init__(self,data):
        self.data = data
        self.nxt = None
class SinglyLL:
    def __init__(self):
        self.head = None
    def create(self):
        n = int(input("Enter no of nodes:"))
        head = Node(int(input("Enter head node:")))
        current = head
        while n>1:
            current.nxt = Node(int(input("Enter node items:")))
            current = current.nxt
            n-=1
        return head
    def display(self,head):
        current = head
        if self.head is None:
            print("Empty list")
            return
        while current:
            print(current.data,end='->')
            current = current.nxt
        print("None")
s1 = SinglyLL()
s1.display(s1.create())