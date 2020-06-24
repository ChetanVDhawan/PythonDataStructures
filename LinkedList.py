class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def add(self, data):
        node = Node(data)
        if self.start is None:
            self.start = node
            return
        temp = self.start
        while temp is not None:
            temp = temp.next
        temp = node

    def print(self):
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    l1 = LinkedList()
    l1.add("Chetan")
    l1.print()




