import Spaceship


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def delfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def dellast(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def insert_at_index(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.head
        for _ in range(index -1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def delete_at_index(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.delfirst()
        if index == self.length - 1:
            return self.dellast()

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


# TODO : Write function insertatindex to insert a newnode at any given index. Consider all edge cases, including missing nodes.
# TODO : Write fucntion deleteatindex to delete a newnode at any given index. COnsider all edge cases, including missing nodes.
# Make sure to reuse existing function for the correct edge cases for both TODOs
# Write appropriate test function below to test for the new functions.

def testing_linked_list():
    from Spaceship import Spaceship

    s1 = Spaceship("Voyager", 300)
    s2 = Spaceship("Enterprise", 300)
    s3 = Spaceship("Atlantis", 300)
    s4 = Spaceship("Challenger", 300)
    s5 = Spaceship("Artemis", 300)

    mylinkedlist = LinkedList(s1)
    mylinkedlist.append(s2)
    mylinkedlist.append(s3)
    mylinkedlist.prepend(s4)
    mylinkedlist.prepend(s5)
    mylinkedlist.print_list()

    s6 = Spaceship("Prometheus", 300)
    mylinkedlist.insert_at_index(3,s6)
    mylinkedlist.print_list()

    mylinkedlist.delete_at_index(4)
    mylinkedlist.print_list()

testing_linked_list()