# My best linked list version

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at(self, position, value):
        if position < 0 or position > self.get_len():
            raise Exception('[-] Invalid index')
        if position == 0:
            self.insert_at_begining(value)
        else:
            count = 0
            node = self.head
            while count < position - 1:
                node = node.next
                count += 1
            new_node = Node(value, node.next)
            node.next = new_node
            if new_node.next is None:
                self.tail = new_node

    def insert_at_begining(self, value):
        node = Node(value, self.head)
        self.head = node

    def insert_at_end(self,value):
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)
            self.tail = node.next
            print(self.tail)

    def create_new_linked_list(self, llist):
        self.head = None
        for element in llist:
            self.insert_at_end(element)

    def get_len(self):
        node = self.head
        index = 0 
        while node:
            node = node.next
            index += 1 
        return index

    def remove_at_position(self, position):
        if position < 0 or position > self.get_len():
            raise Exception("[-] Invalid index")
        else:
            node = self.head
        if position == 0:
            self.head = self.head.next
        elif position == 1:
            if node.next.next is None:
                self.head.next = None
                self.tail = self.head
            else:
                node.next = node.next.next
        else:
            count = 0
            while count < position - 1:
                node = node.next
                count += 1 
            if node.next == self.tail:
                node.next = None
                self.tail = node
            else:
                node.next = node.next.next

    def print(self):
        node = self.head
        llstr = ""
        while node:
            llstr += str(node.value) + "-->"
            node = node.next
        print(llstr)

    def __iter__(self):
        if self.head is None:
            print('[-] List is empty')
        else:
            node = self.head
            while node:
                yield node
                node = node.next



def main():
    if __name__ == '__main__':
        list = LinkedList()
        list.insert_at_begining(0)
        list.insert_at_begining(1)
        list.insert_at_begining(2)
        list.insert_at_begining(3)
        list.insert_at_end(100)
        list.insert_at_end(200)
        list.insert_at_end(300)
        print([node.value for node in list])
        list.create_new_linked_list(['tomato', 'banana', 'bread', 'one', 'two'])
        list.print()
        print(list.get_len())
        list.create_new_linked_list(['one', 'two'])
        list.remove_at_position(1)
        list.print()
        list.create_new_linked_list(['tomato', 'banana', 'bread', 'one', 'two'])
        list.print()
        list.remove_at_position(1)
        list.print()
        list.create_new_linked_list(['tomato', 'banana', 'bread'])
        list.print()
        list.remove_at_position(2)
        list.print()
        list.insert_at(1, 100)
        list.print()

main()
