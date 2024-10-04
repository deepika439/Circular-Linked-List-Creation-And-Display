class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.temp=None

    def create(self):
        size=int(input())
        for i in range(size):
            value=int(input())
            newnode = Node(value)

            if self.head==None:
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                self.temp=newnode
            self.temp.next=self.head

    def display(self):
        self.temp=self.head
        while self.temp.next!=self.head:
            print(self.temp.data)
            self.temp=self.temp.next
        print(self.temp.data)

obj=CircularLinkedList()
obj.create()
obj.display()
