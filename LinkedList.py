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
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def pop(self):
        if self.start is None or self.start.next is None:
            self.start = None
            print("[]")
            return
        temp = self.start
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete(self,data):
        if self.start is None:
            print("Nothing to delete")
        if self.start.data == data:
            self.start = self.start.next
        temp = self.start
        while temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp =temp.next
        print("Data isnt in list")

    def length(self):
        count = 0
        temp = self.start
        while temp is not None:
            count=count+1
            temp = temp.next
        print(f"count is {count}")
        return count


    def insert(self,position,data):
        count = 0
        node = Node(data)
        if position == 0:
            self.start,self.start.next = node,self.start

            return
        temp = self.start
        while temp is not None:
            if position > 0 and position <= self.length():
                if count == position -1:
                    temp.next, temp.next.next = node, temp.next
            else:
                print("Index out of bounds")
                return
            temp = temp.next
            count = count + 1

    def print(self):
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    l1 = LinkedList()
    l1.add("Chetan")
    l1.add("Dhawan")
    l1.add("Prasad")
    l1.add("yui")
    l1.add("Raj")
    l1.delete("hasdhs")
    l1.print()
    print("=============")
    l1.length()
    l1.insert(5,"DID")
    l1.print()
    print("=============")






