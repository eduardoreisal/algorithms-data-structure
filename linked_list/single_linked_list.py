class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, position):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if position == 0:
                new_node.next = self.head
                self.head = new_node
            elif position == 1:
                new_node.next = self.head.next
                self.head.next = new_node
            else:
                temp_node = self.head
                index = 0
                while index < position - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if new_node.next is None:
                    self.tail = new_node

    def loop(self):
        node = self.head
        if node is None:
            print('Empty list')
        else:
            while node:
                print(node.value)
                node = node.next

    def search_value(self, value):
        node = self.head
        if node is None:
            print('Empty List')
        else:
            while node:
                if node.value == value:
                    print('[+] Value found!')
                    break
                node = node.next
            print('[-] Value not found')

    def delete(self, position):
        if self.head is None:
            print("[+] Linked List is empty")
        else:
            if position == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            # NOTE: Check this later. Looks like something is wrong
            elif position == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < position - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next


def add_to_linked_list():
    linked_list = LinkedList()
    [linked_list.insert(num, num) for num in range(3)]
    while True:
        option = int(input("[+] 1 to see list. 2 To add num. 3 to delete: "))
        match option:
            case 1:
                print([node.value for node in linked_list])
            case 2:
                print('[+] Adding num to linked list')
                value = int(input('[+] Enter value: '))
                location = int(input('[+] Enter location: '))
                linked_list.insert(value, location)
            case 3:
                print('[+] Pick index to delete')
                index = int(input('Enter index: '))
                linked_list.delete(index)

add_to_linked_list()
