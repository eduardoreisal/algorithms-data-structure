class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node

    def __iter__(self):
        node = self.head
        count = 0
        while node:
            yield node
            node = node.next
            if node == self.head:
                if count > 0:
                    break
                count += 1

    def insert_at(self, value, location):
        if self.head is None:
            create(value)
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

circular_list = CircularLinkedList()
circular_list.create(1)

print([node.value for node in circular_list])
