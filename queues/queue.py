class ArrayQueue:
    """FIFO queue implementation using a python list as uderlying storage"""
    DEFAULT_CAPACITY = 10 # Capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return true if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return but do not remove the element at the front of the queue
        Raise exception if queue is empty"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue 
        Raise Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._date[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        return answer

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        if self._size == len(self._data):
            self.resize(2 * len(self.data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def show(self):
        return self._data

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)"""
        old = self._data
        self._data = [None] * cap
        wlak = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + wal) % len(old)
        self._front = 0

queue = ArrayQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

print(queue.show())
