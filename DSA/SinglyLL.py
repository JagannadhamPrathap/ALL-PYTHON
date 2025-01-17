class Node:
    def __init__(self,data):
        self.data = data
        self.nxt = None
class SingleLL:
    def __init__(self):
        self.head = None
    def length(self,head):
        if head is None:
            return 0
        return 1+self.length(head.nxt)
    def ins_end(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.nxt:
            current = current.nxt
        current.nxt = node
    def ins_begin(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.nxt = self.head
        self.head = node
    def ins_pos(self):
        pos = int(input())
        data = int(input())
        node = Node(data)
        current = self.head
        if pos == 0:
            self.ins_begin(data)
            return
        for i in range(pos-1):
            current = current.nxt
        if current is None:
            print("Index out of range")
            return
        node.nxt = current.nxt
        current.nxt = node
    def delete_pos(self):
        pos = int(input())
        if self.head is None:
            print("Empty list")
            return
        current = self.head
        if pos == 0:
            self.head = current.nxt
            current = None
            return
        prev = None
        count = 0
        while current and count != pos:
            prev = current
            current = current.nxt
            count+=1
        if current is None:
            print("Index out of range")
            return 
        prev.nxt = current.nxt
        current = None
    def delete_ele(self):
        ele = int(input())
        if self.head is None:
            print("Empty list")
            return 
        current = self.head
        if current and current.data == ele:
            self.head = current.nxt
            current = None
            return
        prev = None
        while current and current.data!=ele:
            prev = current
            current = current.nxt
        if current is None:
            print("Element not found")
            return
        prev.nxt = current.nxt
        current = None
    def search(self,data):
        if self.head is None:
            print('Empty list')
        current = self.head
        count = 0
        while current and current.data!=data:
            current = current.nxt
            count+=1
        if current is None:
            print("Not found")
        else:
            print(f"Found element at {count}")
    def search_recur(self,node,key):
        if node is None:
            return 'Not found'
        if node.data == key:
            return 'Found element'
        return self.search_recur(node.nxt,key)
    def rev_recur(self,node):
        if node is None:
            return None
        self.rev(node.nxt)
        print(node.data,end='->')
    def rev(self):
        prev = None
        if self.head is None:
            print("Empty list")
            return
        current = self.head
        while current:
            temp = current.nxt
            current.nxt = prev
            prev = current
            current = temp
        self.head = prev
    def display(self):
        if self.head is None:
            print("None")
        current = self.head
        while current:
            print(current.data,end='->')
            current = current.nxt
        print("None")
sl = SingleLL()
sl.display()
sl.ins_begin(5)
sl.ins_begin(9)
sl.ins_begin(77)
sl.display()
sl.ins_end(21)
sl.ins_end(10)
sl.display()
# sl.delete_pos()
# sl.display()
# sl.ins_end(23)
# sl.display()
# sl.delete_ele()
# sl.display()
# sl.ins_pos()
# sl.display()
# sl.search(11)
# print(sl.search_recur(sl.head,23))
# print(sl.length(sl.head))
# sl.rev(sl.head)
sl.rev()
sl.display()