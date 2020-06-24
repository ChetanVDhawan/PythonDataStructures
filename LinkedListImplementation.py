class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def insert_values(self, fruitlist):
        for fruit in fruitlist:
            newnode = Node(fruit)
            if self.start is None:
                self.start = newnode
            else:
                temp = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.next = newnode

    def insert_after_value(self, before, after):
        if self.start is None:
            print("Cant insert data as there is no data")
            return
        newnode = Node(after)

        temp = self.start
        while temp.data != before:
            temp = temp.next

        temp.next, newnode.next = newnode, temp.next

    def printl(self):
        if self.start is None:
            print("There is not data")
            return
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def remove_by_value(self, fruit_name):
        temp = self.start
        if temp is None:
            print("There is no data")
        while temp.next is not None:
            if temp.next.data == fruit_name:
                temp.next = temp.next.next
                break
            temp = temp.next
        print("Fruit Not Found")
