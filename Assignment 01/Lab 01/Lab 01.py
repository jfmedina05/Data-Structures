class LinkedList:
    def __init__(self, num, next):
        self.num = num
        self.next = next
    def insert(self, num):
        if self.next == None:
            self.next = LinkedList(num, None)
        else:
            self.next.insert(num)

Node = LinkedList(6, LinkedList(7, None))

Node.insert(8)

print(Node.next.next.num)