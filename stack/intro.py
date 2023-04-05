class ArrayStack:
    """LIFO Stack implementation using a python list as underlying storage."""
    def __init__(self):
        """Create an empty task"""
        self._data = []

    def __len__(self):
        """Return True if the stack is empty."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack (i.e, LIFO)
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

# It's possible to use the stack to revert files
def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'W')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close


# stack = ArrayStack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)
# print(len(stack))
# print(stack.top())
